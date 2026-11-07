"""AI-assisted vowel-counting demonstration using synthetic input."""
import json
import sys
from collections import Counter
from pathlib import Path


def count_vowels(path):
    counts = Counter(Path(path).read_text(encoding="utf-8").lower())
    return {v: counts[v] for v in "aeiou"}


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python practice_frequency.py FILE")
    try:
        print(json.dumps(count_vowels(sys.argv[1]), sort_keys=True))
    except (OSError, UnicodeError) as exc:
        sys.exit(str(exc))
