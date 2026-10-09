# Project 1: Turn department categories into columns

This first, deliberately small project continues from the pandas question about `pd.get_dummies()` and `reviews.join(one_hot)`. It shows how one category column becomes several 0/1 columns. It does **not** train a machine-learning model yet.

## Run it

1. Open a Terminal window and move into this project folder. If you cloned the whole learning repository, start at its root and run:

   ```bash
   cd projects/01-one-hot-encoding
   ```

   If you downloaded this project folder by itself, use `cd` with the location where you saved that folder.

2. (Recommended) Create and activate a small Python environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the one library this project uses:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Run the program:

   ```bash
   python main.py
   ```

Read [the lesson](lesson.md) alongside the code. The CSV contains tiny, invented practice data; it is not real customer data.
