import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from practice_frequency import count_vowels
from practice_pipeline import generate
from practice_todo import Task, TaskPool


class FrequencyTests(unittest.TestCase):
    def test_counts_case_and_zeroes(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "data.txt"
            p.write_text("AaEei! OUu xyz", encoding="utf-8")
            self.assertEqual(count_vowels(p), dict(a=2, e=2, i=1, o=1, u=2))

    def test_empty_input(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "data.txt"
            p.write_text("", encoding="utf-8")
            self.assertEqual(count_vowels(p), dict.fromkeys("aeiou", 0))

    def test_missing_file(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(FileNotFoundError):
                count_vowels(Path(d) / "missing")

    def test_cli_usage_fails(self):
        p = subprocess.run([sys.executable, str(Path(__file__).with_name("practice_frequency.py"))], capture_output=True)
        self.assertNotEqual(p.returncode, 0)
        self.assertIn(b"Usage:", p.stderr)


class TaskTests(unittest.TestCase):
    def test_add_task(self):
        pool = TaskPool()
        task = Task("Review API contract")
        pool.add_task(task)
        self.assertEqual(pool.tasks, [task])

    def test_complete_and_filter(self):
        pool = TaskPool()
        task = Task("Review")
        pool.add_task(task)
        self.assertEqual(pool.get_open_tasks(), [task])
        task.mark_completed()
        task.mark_completed()
        self.assertTrue(task.completed)
        self.assertEqual(pool.get_open_tasks(), [])
        self.assertEqual(pool.get_done_tasks(), [task])

    def test_populate(self):
        pool = TaskPool()
        pool.populate()
        pool.populate()
        self.assertEqual(len(pool.tasks), 6)
        self.assertEqual(len(pool.get_open_tasks()), 3)
        self.assertEqual(len(pool.get_done_tasks()), 3)

    def test_invalid_task(self):
        for args in [("",), (" ",), ("x", "Unknown")]:
            with self.assertRaises(ValueError):
                Task(*args)
        with self.assertRaises(TypeError):
            TaskPool().add_task("not a task")

    def test_display(self):
        t = Task("Review", "Done")
        self.assertEqual(repr(t), "Review - Done")
        self.assertEqual(str(t), "Task: Review, Status: Done")
        self.assertTrue(t.completed)


class PipelineTests(unittest.TestCase):
    def test_outputs_escape_and_append(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "input.txt"
            p.write_text("AEIOU", encoding="utf-8")
            out = Path(d) / "out"
            result = generate(p, out, "<script>alert(1)</script>", "test-version")
            self.assertEqual(result["vowels"], dict.fromkeys("aeiou", 1))
            self.assertEqual(json.loads((out / "result.json").read_text()), result)
            self.assertNotIn("<script>", (out / "index.html").read_text())
            generate(p, out, "second-run", "next-version")
            self.assertEqual((out / "README.md").read_text().count("### Updated at"), 2)

    def test_missing_input_no_output(self):
        with tempfile.TemporaryDirectory() as d:
            out = Path(d) / "out"
            with self.assertRaises(FileNotFoundError):
                generate(Path(d) / "missing", out, "test", "test")
            self.assertFalse(out.exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
