"""Synthetic local-history fixtures; never read or modify the user's history."""

import json
import os
from pathlib import Path
import sqlite3
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).with_name("ai_sessions.py")


class SessionTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.home = Path(temporary.name)
        self.codex = self.home / "custom codex # home"
        self.codex.mkdir()
        self.env = {**os.environ, "HOME": str(self.home), "CODEX_HOME": str(self.codex)}

    def run_cli(self, *args):
        return subprocess.run([sys.executable, "-I", str(SCRIPT), *args],
                              env=self.env, text=True, capture_output=True)

    def list_cli(self, *args):
        return self.run_cli("list", "--since", "2026-01-01", "--until", "2026-01-02", *args)

    def transcript(self, path, source):
        path.parent.mkdir(parents=True, exist_ok=True)
        rows = []
        for role, text in (("user", "Find ABC-123"), ("assistant", "Result verified")):
            message = {"role": role, "content": [{"type": "text", "text": text}]}
            rows.append({"timestamp": "2026-01-01T12:00:00Z", "type": role,
                         "cwd": "/example/sample-app", "message": message} if source == "claude" else
                        {"timestamp": "2026-01-01T12:00:00Z", "type": "response_item",
                         "payload": {"type": "message", **message}})
        path.write_text("\n".join(json.dumps(row) for row in rows) + "\n")
        return path

    def database(self, name="state_9.sqlite"):
        path = self.codex / name
        with sqlite3.connect(path) as connection:
            connection.execute("create table threads (id,title,cwd,created_at,updated_at,archived,"
                               "rollout_path,first_user_message,git_branch,source)")
            rollout = self.transcript(self.home / "exports/rollout.jsonl", "codex")
            for tid, archived, source in (("active", 0, None), ("archived", 1, "cli"),
                                           ("child", 0, '{"subagent":"worker"}')):
                connection.execute("insert into threads values (?,?,?,?,?,?,?,?,?,?)",
                                   (tid, "Example", "/example/sample-app", 1767268800, 1767268800,
                                    archived, str(rollout), "Find work", "main", source))
        return path

    def test_custom_codex_home_latest_database_and_read_only(self):
        old = self.database("state_5.sqlite")
        with sqlite3.connect(old) as connection:
            connection.execute("update threads set title='Stale database'")
        latest = self.database("state_10.sqlite")
        before = {p: p.read_bytes() for p in (old, latest)}
        result = self.list_cli("--source", "codex")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("| active", result.stdout)
        self.assertNotIn("Stale database", result.stdout)
        self.assertNotIn("| archived", result.stdout)
        self.assertNotIn("| child", result.stdout)
        archived = self.list_cli("--source", "codex", "--include-archived", "--grep", "ABC-123", "--deep")
        self.assertEqual(archived.returncode, 0, archived.stderr)
        self.assertIn("| archived", archived.stdout)
        for path, content in before.items():
            self.assertEqual(path.read_bytes(), content)

    def test_missing_source_is_partial_coverage_not_empty_success(self):
        self.transcript(self.home / ".claude/projects/example/claude-1.jsonl", "claude")
        result = self.list_cli()
        self.assertEqual(result.returncode, 1)
        self.assertIn("| claude-1", result.stdout)
        self.assertIn("sources searched: claude; unavailable: codex", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_schema_mismatch_does_not_fall_back_to_stale_database(self):
        self.database("state_5.sqlite")
        with sqlite3.connect(self.codex / "state_10.sqlite"):
            pass
        result = self.list_cli("--source", "codex")
        self.assertEqual(result.returncode, 1)
        self.assertIn("history unavailable", result.stderr)
        self.assertEqual(result.stdout, "")

    def test_show_export_detects_format_from_content(self):
        for source in ("claude", "codex"):
            path = self.transcript(self.home / f"exports/{source}.jsonl", source)
            path.write_text("null\n[1]\n" + path.read_text() + "{partial line\n")
            result = self.run_cli("show", str(path))
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("U: Find ABC-123", result.stdout)
            self.assertIn("A: Result verified", result.stdout)

    def test_show_unknown_id_is_clean_error_without_creating_database(self):
        result = self.run_cli("show", "missing-session")
        self.assertEqual(result.returncode, 1)
        self.assertIn("no Codex history database", result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        self.assertEqual(list(self.codex.iterdir()), [])

    def test_show_ambiguous_claude_prefix_is_rejected(self):
        for name in ("same-one", "same-two"):
            self.transcript(self.home / f".claude/projects/example/{name}.jsonl", "claude")
        result = self.run_cli("show", "same-")
        self.assertEqual(result.returncode, 2)
        self.assertIn("ambiguous", result.stderr)

    def test_deep_search_missing_rollout_reports_failure(self):
        self.database()
        (self.home / "exports/rollout.jsonl").unlink()
        result = self.list_cli("--source", "codex", "--grep", "ABC-123", "--deep")
        self.assertEqual(result.returncode, 1)
        self.assertIn("transcript unavailable", result.stderr)

    def test_invalid_arguments_and_unknown_transcript_are_clean_errors(self):
        unknown = self.home / "unknown.jsonl"
        unknown.write_text('{"type":"unsupported"}\n')
        for args, status in ((("show", str(unknown)), 1),
                             (("show", str(unknown), "--max-chars", "0"), 2),
                             (("list", "--since", "2026-02-01", "--until", "2026-01-01"), 2)):
            result = self.run_cli(*args)
            self.assertEqual(result.returncode, status)
            self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
