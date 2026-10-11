# Lesson 3 — Choose numeric features before scaling

**Today’s goal:** Safely choose numeric measurements, scale them with `StandardScaler`, and understand what the scaler learns.

**Pace:** We are still preparing data. This project does not train or evaluate a prediction model.

## 1. How this connects to the last lessons

In lesson 1, `pd.get_dummies()` turned each department name into a separate 0/1 flag. In lesson 2, we compared that with integer codes and asked whether a category really has an order.

Today, we’ll look at columns that already contain numbers. They still need thought before we give them to a model. Some numbers measure something; other numbers are just labels written with digits.

The CSV has six tiny, **invented practice rows**. It is not real customer or review data, and it is not a training set for a real product.

## 2. Numeric does not automatically mean useful measurement

The data contains these numeric columns:

- `review_id`: identifies a row. The values 1001, 1002, and 1003 do not mean one review is larger, better, or farther from another. This is an identifier.
- `review_rating`: a numeric rating from 1 to 5. Here it is a measurement we want to practice scaling.
- `days_to_review`: a count of days. This is also a measurement we want to practice scaling.

Pandas can find columns whose stored values are numeric:

```python
numeric_columns = reviews.select_dtypes(include="number").columns.tolist()
```

But that may include `review_id`. `select_dtypes` answers “which columns have numeric data types?” It cannot decide which columns make sense as model inputs. We should choose the columns intentionally:

```python
feature_columns = ["review_rating", "days_to_review"]
numeric_features = reviews[feature_columns]
```

A **feature** is an input value we might use to help a model make a prediction. An identifier is usually not a meaningful measurement feature just because it has digits. Always ask what a column means, not only what type it has.

## 3. Why scale numeric features?

The selected columns use different ranges and units. `review_rating` is between 1 and 5 in this sample; `days_to_review` ranges from 1 to 14. Some machine-learning methods use distances or compare the sizes of numbers. If one feature has much larger values, it can have more influence simply because of its scale.

`StandardScaler` converts each selected value into a **standard score**, also called a **z-score**:

```text
z = (value - column mean) / column standard deviation
```

After this transformation, each selected column is centered around 0 and has a population standard deviation around 1 for the data used to fit the scaler.

- A value near `0` is near that column’s average.
- A positive value is above the average.
- A negative value is below the average.
- The value is measured in standard deviations from the average, not in the original unit (stars or days).

The scaled value is not a probability, rating, or model prediction. Scaling changes the representation of the inputs; it does not tell us whether a review is good or bad.

## 4. Walk through the code

### Load and inspect the data

```python
data_path = Path(__file__).parent / "data" / "reviews.csv"
reviews = pd.read_csv(data_path)
```

`Path(__file__).parent` means “the folder containing this Python script.” We build the CSV path from there so the project can run from different folders. `read_csv` loads the comma-separated rows into a pandas DataFrame.

### Ask pandas which columns are numeric

```python
numeric_columns = reviews.select_dtypes(include="number").columns.tolist()
```

`select_dtypes` filters columns by stored data type. `.columns` retrieves the selected column names, and `.tolist()` turns those names into a regular Python list. You should see `review_id`, `review_rating`, and `days_to_review`.

That output is a useful warning: automatically scaling every numeric column could also scale the ID. The script prints the detected columns so you can see the distinction.

### Pick the measurements explicitly

```python
feature_columns = ["review_rating", "days_to_review"]
numeric_features = reviews[feature_columns]
```

The list records our decision. Pandas selects those two columns and keeps the row order. `review_id`, `department_name`, and `condition` remain outside this scaling step.

### Create the scaler and apply it

```python
scaler = StandardScaler()
scaled_array = scaler.fit_transform(numeric_features)
```

`StandardScaler()` creates the transformer. `fit_transform(...)` does two related jobs:

1. **Fit:** calculate and remember a mean and standard deviation for each selected column.
2. **Transform:** subtract each column’s mean and divide by its standard deviation, returning the converted numbers.

The scaler stores those learned statistics in `scaler.mean_` and `scaler.scale_`; the program prints them. `scale_` is the divisor the scaler uses for each feature. For a column with no variation, scikit-learn handles the zero-variance case without dividing by zero.

Here, “fit” means the preprocessing tool calculates its settings from example values. It does **not** mean we trained a model to predict a target. There is no target column and no prediction model in this project.

The result from scikit-learn is a NumPy array. Arrays do not carry pandas column names, so the next code wraps those values back into a DataFrame:

```python
scaled_features = pd.DataFrame(
    scaled_array,
    columns=feature_columns,
    index=reviews.index,
)
```

`columns=...` restores the feature names. `index=...` preserves the original row labels, so the scaled values stay aligned with the same reviews.

### Check the result

```python
scaled_features.mean()
scaled_features.std(ddof=0)
```

The first check should be close to zero for each column; the second should be close to one. `ddof=0` asks pandas for the population standard deviation, matching the convention used by `StandardScaler`. Tiny display differences can occur from rounding.

## 5. Why not scale the entire DataFrame?

The full table includes text categories such as `department_name` and `condition`. A scaler needs numeric values, so giving it the entire table can cause a conversion error. Even if every column were numeric, scaling IDs or unrelated counts might be a bad choice.

This is why we first make a feature list and pass only those columns to `fit_transform`. It makes the intention visible and avoids accidentally sending text or identifiers into the scaler.

## 6. Practice data versus training data

This file is **practice data**: we invented it to learn what the code does. Since there is no target and no model, it is not training data for a prediction task.

In future supervised learning, a dataset usually has:

- **Features (`X`)** — the inputs, such as a rating or a product category.
- **Target (`y`)** — the answer the model is meant to predict, such as a label.
- **Training split** — examples used to fit the prediction model.
- **Test split** — separate examples held back to estimate performance after training.

A preprocessing transformer can also learn from data. Once we have a training/test split, the safe order is:

```python
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train[feature_columns])
X_test_scaled = scaler.transform(X_test[feature_columns])
```

Fit the scaler on the training features only. Then use that same scaler to transform the test features. If we calculate the mean and standard deviation using both training and test rows, information from the held-back test set influences preprocessing. That is a form of **data leakage** and can make a later evaluation less trustworthy.

Our small script calls `fit_transform` on all six rows only to make the calculation easy to inspect. It does not claim to estimate real model performance. When we reach a real train/test workflow, we’ll adjust the code to fit the scaler only on the training split.

## 7. What scaling does not guarantee

Scaling puts features on a comparable standard-score scale. It does not guarantee that a model will become more accurate, and the lesson does not measure any model performance. Some algorithms are sensitive to feature scale; others, such as many tree-based methods, generally do not depend on the same distance or magnitude comparisons.

Standard scaling can also be influenced by unusually extreme values because the mean and standard deviation respond to outliers. Later, we can compare other approaches once we have a reason to use them.

## 8. Run it and explore

From this project folder, install the packages and run:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

Then try these small experiments:

1. Add a `review_id` column to `feature_columns`. Notice how an identifier can be mathematically scaled even though that does not make it a sensible measurement.
2. Remove `days_to_review` from `feature_columns`. The script should scale only `review_rating` because the same explicit list controls both selection and output names.
3. Change one practice rating and rerun the script. The learned mean and the scaled values will change because the scaler is fitted on those rows.

## 9. Words to keep

- **Numeric data type:** a storage type that pandas recognizes as numbers; it does not prove a column is a meaningful feature.
- **Identifier:** a value used to distinguish records, such as `review_id`.
- **Feature:** an input column used by a model.
- **Scaling / standardization:** changing numeric features to a chosen scale.
- **Mean:** the arithmetic average of values.
- **Standard deviation:** a measure of how spread out values are around their mean.
- **Standard score / z-score:** a value expressed in standard deviations from a mean.
- **Transformer:** a preprocessing tool that learns or applies a consistent data conversion.
- **Data leakage:** information from outside the training split influencing model fitting or evaluation.

## 10. How this fits the learning path

We have now encoded unordered categories, compared meaningful and arbitrary category order, and chosen numeric features before scaling them. We still have not trained a prediction model. A gradual next step is to practice separating input features from a target and splitting invented examples before building a first small model.

## References

- [scikit-learn `StandardScaler` API](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)
- [scikit-learn common pitfalls: data leakage](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage)
