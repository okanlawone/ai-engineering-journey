from pathlib import Path

import pandas as pd
from sklearn.preprocessing import StandardScaler


# Load the small, invented practice dataset beside this program.
data_path = Path(__file__).parent / "data" / "reviews.csv"
reviews = pd.read_csv(data_path)

print("Practice data (invented examples):")
print(reviews.to_string(index=False))

# This finds every column pandas considers numeric. Notice that review_id
# appears here too, even though it is only an identifier.
numeric_columns = reviews.select_dtypes(include="number").columns.tolist()
print("\nColumns pandas recognizes as numeric:")
print(numeric_columns)

# Choose measurements on purpose. Do not scale review_id: its digits identify
# a row and do not measure a review's rating or waiting time.
feature_columns = ["review_rating", "days_to_review"]
numeric_features = reviews[feature_columns]

# fit_transform learns each selected column's mean and standard deviation,
# then converts the values into standard scores (z-scores).
scaler = StandardScaler()
scaled_array = scaler.fit_transform(numeric_features)

# scikit-learn returns an array. Wrap it in a DataFrame to restore the useful
# column names and the original row index.
scaled_features = pd.DataFrame(
    scaled_array,
    columns=feature_columns,
    index=reviews.index,
)

print("\nMeasurements selected for scaling:")
print(numeric_features.to_string(index=False))

print("\nThe means learned by the scaler:")
print(pd.Series(scaler.mean_, index=feature_columns).round(3))
print("\nThe standard deviations learned by the scaler:")
print(pd.Series(scaler.scale_, index=feature_columns).round(3))

print("\nScaled measurements (approximately centered around zero):")
print(scaled_features.round(3).to_string(index=False))

print("\nCheck: scaled-column means (approximately zero):")
print(scaled_features.mean().round(6))
print("\nCheck: scaled population standard deviations (approximately one):")
print(scaled_features.std(ddof=0).round(6))
