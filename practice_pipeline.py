"""Generate an escaped static demonstration from synthetic fixtures."""
import argparse
import html
import json
from datetime import datetime, timezone
from pathlib import Path
from practice_frequency import count_vowels
from practice_todo import TaskPool


def generate(source, output, actor, commit):
    counts = count_vowels(source)  # Fail before writing if input is invalid.
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    pool = TaskPool()
    pool.populate()
    result = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "actor": actor, "commit": commit, "vowels": counts,
        "todo": [t.title for t in pool.get_open_tasks()],
        "done": [t.title for t in pool.get_done_tasks()],
        "attribution": "AI-assisted demo; all task statuses are synthetic fixtures",
    }
    (output / "result.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    page = ('<!doctype html><html lang="en"><meta charset="utf-8">'
            '<title>AI product workflow practice</title><body>'
            '<h1>AI product workflow practice</h1>'
            '<p>AI-assisted demonstration with synthetic data. No personal data or live API calls.</p>'
            '<pre>' + html.escape(json.dumps(result, indent=2)) + '</pre></body></html>')
    (output / "index.html").write_text(page, encoding="utf-8")
    with (output / "README.md").open("a", encoding="utf-8") as f:
        f.write(f"\n### Updated at {result['timestamp_utc']}\n")
        f.write("```json\n" + json.dumps(result, indent=2) + "\n```\n")
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default="practice_data.txt")
    parser.add_argument("--output", default="practice-report")
    parser.add_argument("--actor", default="demo-runner")
    parser.add_argument("--commit", default="unversioned")
    args = parser.parse_args()
    print(json.dumps(generate(args.file, args.output, args.actor, args.commit), indent=2))
