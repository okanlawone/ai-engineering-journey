from pathlib import Path

import pandas as pd


# Find the CSV beside this program, so it works from any current folder.
data_path = Path(__file__).parent / "data" / "reviews.csv"
reviews = pd.read_csv(data_path)

print("Original reviews table:")
print(reviews)

# Each distinct department becomes its own 0/1 column.
one_hot = pd.get_dummies(
    reviews["department_name"],
    prefix="dept",
    dtype=int,
)

print("\nNew one-hot table:")
print(one_hot)

# Join the new columns to reviews using each row's matching index.
reviews = reviews.join(one_hot)

print("\nCombined table:")
print(reviews)

print("\nColumn names:")
print(reviews.columns.tolist())
