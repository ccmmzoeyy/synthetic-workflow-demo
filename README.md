# Synthetic workflow demo

A small AI-assisted Python demonstration: count vowels, model synthetic tasks, test edge cases, and generate a static HTML page. All task statuses are sample fixtures, not real project progress.

This standalone repository contains no coursework submissions, personal documents, research data, API keys, external API calls or references to a private portfolio. It is not a production application or a claim of independent authorship.

## Run

```sh
python3 practice_tests.py
python3 practice_pipeline.py --file practice_data.txt --output site --actor demo-runner --commit demo-v1
```

The 11 tests cover vowel counting, missing input, task state, JSON output, HTML escaping and append-only report output. The `site` directory is generated locally; only its HTML page and JSON sample are used for the public static preview.

## Deployment

GitHub Pages serves `index.html` from the main branch root. The checked-in page is a snapshot of a real generator run over synthetic input. Source changes do not regenerate it automatically: rerun the command above and copy `site/index.html` and `site/result.json` to the root before committing.

AI assistance was used to write, test and package this demonstration. There are no analytics, forms, cookies or third-party resources in the page itself.
