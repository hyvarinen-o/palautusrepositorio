# Repository notes

- This directory is a standalone Python project (Python `>=3.14`); run commands from here and use `uv` so the locked project environment is used.
- Run the focused suite with `uv run --group dev pytest src/tests/ostoskori_test.py` (the tests use `unittest` assertions but are run with pytest).
- Core shopping-cart classes are in `src/`: `Ostoskori` is the cart, `Ostos` represents a product and quantity, and `Tuote` represents a product. Tests live in `src/tests/`.
- Code of `Ostos` and `Tuote` should not be changed
- Code of tests inside `src/tests/` should not be changed unless explicitly asked
- Always implement absolute minimal code that makes the tests pass