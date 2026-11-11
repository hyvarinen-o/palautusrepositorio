# Project notes

- Python requirement is 3.14 (`.python-version`). Install/sync dependencies from this directory with `uv sync`.
- The Flask app starts via `uv run python src/index.py` and listens on `localhost:5001` (keep it running in a separate terminal for browser tests).
- Robot Framework suites are in `src/tests`. Run all with `uv run robot src/tests`, or one suite, e.g. `uv run robot src/tests/login.robot`.
- Browser tests use Robot Framework Browser/Playwright and default to a visible Chromium window. If browser binaries are missing, install them with `uv run rfbrowser install`; run headlessly with `uv run robot -v HEADLESS:true src/tests`.
- Tests reset state through `/tests/reset`; users are stored in memory in `src/repositories/user_repository.py`, so state does not survive an app restart.
