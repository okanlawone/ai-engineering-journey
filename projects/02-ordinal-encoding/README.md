# Project 2: When should a category become a number?

This project compares two ways to encode categories:

- Department names have no natural ranking, so the example uses one-hot columns.
- Product condition has a meaningful order, so the example compares a dictionary mapping with scikit-learn's `OrdinalEncoder`.

The data is tiny, invented practice data. This project prepares columns; it does not train a prediction model.

## Run it

If you cloned the whole learning repository, start at its root and run:

```bash
cd projects/02-ordinal-encoding
```

If you downloaded this folder by itself, move into its location in Terminal. Then create an environment and install the dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

Read [the lesson](lesson.md) next to the code. It walks through the category lists and the output one step at a time.
