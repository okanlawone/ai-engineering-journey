from pathlib import Path

import pandas as pd
from sklearn.preprocessing import OrdinalEncoder


# Load the small, invented practice dataset beside this program.
data_path = Path(__file__).parent / "data" / "reviews.csv"
reviews = pd.read_csv(data_path)

print("Original table:")
print(reviews)

# Department names are groups with no natural best-to-worst order.
department_one_hot = pd.get_dummies(
    reviews["department_name"],
    prefix="dept",
    dtype=int,
)

# This list makes an arbitrary order explicit for demonstration.
# It does not mean that one department is better than another.
department_order = ["Bottoms", "Dresses", "Intimate", "Jackets", "Tops", "Trend"]
department_encoder = OrdinalEncoder(
    categories=[department_order],
    dtype=int,
)
reviews["department_code"] = department_encoder.fit_transform(
    reviews[["department_name"]]
).ravel()

# Condition has a meaningful order, from poorest to best.
condition_order = ["Poor", "Fair", "Good", "Excellent"]

# A dictionary lets us write the mapping by hand.
condition_to_code = {
    condition: number
    for number, condition in enumerate(condition_order)
}
reviews["condition_code_manual"] = reviews["condition"].map(condition_to_code)

# OrdinalEncoder applies the same explicit order to the condition column.
condition_encoder = OrdinalEncoder(
    categories=[condition_order],
    dtype=int,
)
reviews["condition_code_encoder"] = condition_encoder.fit_transform(
    reviews[["condition"]]
).ravel()

# Add the one-hot department columns to the original rows.
reviews = reviews.join(department_one_hot)

print("\nDepartment: arbitrary ordinal codes beside one-hot flags:")
print(
    reviews[
        [
            "department_name",
            "department_code",
            "dept_Bottoms",
            "dept_Dresses",
            "dept_Intimate",
            "dept_Jackets",
            "dept_Tops",
            "dept_Trend",
        ]
    ]
)

print("\nCondition: dictionary mapping beside OrdinalEncoder:")
print(
    reviews[
        [
            "condition",
            "condition_code_manual",
            "condition_code_encoder",
        ]
    ]
)

print("\nFinal column names:")
print(reviews.columns.tolist())
