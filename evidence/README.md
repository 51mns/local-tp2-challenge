# Evidence and publication provenance

## Two different events

1. **Historical campaign, 2026-10-07:** the direct-search report records 16,677 distinct states / 10,176,120 original supported minors, all positive. See `HISTORICAL_SEARCH_SUMMARY.json`.
2. **This public packaging run:** the new small checker is tested against exact fixtures and an independently represented recurrence on a bounded tree. Its executed scope is written separately in `PUBLICATION_CHECKS.json`. It does not claim to rerun the whole historical search or re-review all old proofs.

The historical search was exhaustive only to depth 13. Deep paths were selected. The reported all-central minima are finite observations. Same-model reimplementations are not an independent researcher's review.

The compact search summary and the closure-audit manuscript were supplied as research artifacts in the conversation. This first public package includes those records; the historical exhaustive per-state dump is not required by the small checker. Do not confuse the top-level new checker with the optimised historical ten-million-minor search implementation.

The mathematical archive was taken from a frozen owner-supplied source commit. Its content hashes appear in `ARCHIVE_MANIFEST.json`. The release contains no private Git history. Historical embedded source hashes identify provenance, not mathematical validity.

## Public verification commands

Run in macOS/Linux Terminal or VS Code's integrated terminal, or PowerShell on Windows, from the repository root:

```bash
python3 -m unittest discover -s tests -v
python3 check.py --depth 6
```

These commands need only Python 3.10+. `python` may replace `python3` on Windows. They check conventions and finite cases only.
