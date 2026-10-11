# Project 3: Choose numeric features before scaling

This project continues the review-data examples from lessons 1 and 2. It shows why “numeric” does not always mean “a measurement”: `review_id` contains digits, but it is an identifier. The script uses an explicit feature list to scale only `review_rating` and `days_to_review` with scikit-learn's `StandardScaler`.

The six rows are invented practice data. This project demonstrates preprocessing only; it does not train or evaluate a prediction model.

## Run it

If you cloned the full learning repository, start at its root:

```bash
cd projects/03-scaling-numeric-features
```

Then create an environment and install the dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

Read [the lesson](lesson.md) for a step-by-step explanation of numeric columns, feature selection, standard scores, `fit_transform`, and why a future model should fit preprocessing on its training split only.
