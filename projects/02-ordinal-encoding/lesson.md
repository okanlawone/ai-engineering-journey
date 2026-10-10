# Lesson 2 — When does a category have an order?

**Today’s goal:** See when integer codes are useful, when they accidentally suggest a ranking, and how a dictionary mapping compares with scikit-learn’s `OrdinalEncoder`.

**Pace:** We are still preparing data. This project does not train a prediction model.

## 1. Two different kinds of categories

The practice file has two category columns:

- `department_name` contains `Bottoms`, `Dresses`, `Intimate`, `Jackets`, `Tops`, and `Trend`. These are different groups. There is no natural rule saying one department is greater, better, or higher than another.
- `condition` contains `Poor`, `Fair`, `Good`, and `Excellent`. These words do have a sensible low-to-high order for condition.

The rows are invented examples for learning. They are not real reviews or customer records.

The distinction matters because an integer can look like a measurement. If we code `Bottoms` as 0 and `Trend` as 5, a model may treat 5 as greater than 0 even though we only chose those labels as different names.

## 2. One-hot encode the unordered department names

The project keeps the same idea from lesson 1:

```python
department_one_hot = pd.get_dummies(
    reviews["department_name"],
    prefix="dept",
    dtype=int,
)
```

Pandas creates a separate flag column for each department. A row in `Tops` has `1` under `dept_Tops` and `0` under the other department columns. These flags say which group the row belongs to without ranking the groups.

## 3. Make an explicit ordinal code for departments

The next lines deliberately encode the same department column with `OrdinalEncoder`:

```python
department_order = ["Bottoms", "Dresses", "Intimate", "Jackets", "Tops", "Trend"]
department_encoder = OrdinalEncoder(
    categories=[department_order],
    dtype=int,
)
reviews["department_code"] = department_encoder.fit_transform(
    reviews[["department_name"]]
).ravel()
```

Because the category list is in this order, the codes are:

| Department | Code |
|---|---:|
| Bottoms | 0 |
| Dresses | 1 |
| Intimate | 2 |
| Jackets | 3 |
| Tops | 4 |
| Trend | 5 |

Those numbers come from the list we supplied. They do **not** mean Trend is five times more important than Bottoms, or that the departments form a real scale. We chose this order to make the rule visible.

When category names have no meaningful order, one-hot encoding is often the safer representation for models that might use numeric order or distance. Exactly how a model treats the codes depends on the model. One-hot encoding spends one column per category, so it can create many columns when a feature has many unique values.

## 4. The same `OrdinalEncoder` can represent a real rank

For product condition, the order does mean something. The code explicitly writes it from lowest to highest:

```python
condition_order = ["Poor", "Fair", "Good", "Excellent"]
```

The manual dictionary uses that list to assign consecutive numbers:

```python
condition_to_code = {
    condition: number
    for number, condition in enumerate(condition_order)
}
reviews["condition_code_manual"] = reviews["condition"].map(condition_to_code)
```

This is the dictionary approach you have already seen. `enumerate(...)` walks through the list and gives each item its position, starting at 0. So `Poor` becomes 0, `Fair` 1, `Good` 2, and `Excellent` 3.

Now compare it with the scikit-learn encoder:

```python
condition_encoder = OrdinalEncoder(
    categories=[condition_order],
    dtype=int,
)
reviews["condition_code_encoder"] = condition_encoder.fit_transform(
    reviews[["condition"]]
).ravel()
```

The explicit list tells `OrdinalEncoder` which category codes to use, in what order. The code list is wrapped in another list because `OrdinalEncoder` accepts a category list for each input column, and this call gives it one column: `condition`.

For the rows in this practice file, `condition_code_manual` and `condition_code_encoder` should match. One is a mapping we wrote with a dictionary; the other is a reusable scikit-learn transformer configured with the same category order.

## 5. What `fit_transform()` means here

In `fit_transform`, “fit” means the encoder sets up its transformation from the input data and its category instructions; “transform” means it returns the corresponding codes. This is a preprocessing step. It is **not** a predictive model learning to guess review outcomes.

The double brackets are intentional:

```python
reviews[["condition"]]
```

They select a one-column DataFrame. Scikit-learn transformers generally receive a table of input columns. Their result is a two-dimensional array, even when there is only one input column. `.ravel()` flattens that one-column result into a simple one-dimensional sequence so pandas can place it in one DataFrame column.

We set `dtype=int` so the codes print as integers. Without that option, ordinal encoder output commonly uses a numeric array type that can display whole-number codes with decimal points.

## 6. Read the side-by-side output

Run:

```bash
python main.py
```

The first comparison prints each department next to its ordinal code and its one-hot flags. It helps answer two separate questions:

- The one-hot flags answer: “Which department is this row in?”
- The department integer answers: “Which number did our chosen list assign this department?”

The second comparison prints each condition next to both the manual code and the `OrdinalEncoder` code. Those two numbers should agree because both use the same `condition_order`.

The script joins the department flag table back to `reviews`, just like the previous lesson. The join keeps the original row order and attaches matching one-hot values by the shared DataFrame index.

## 7. A subtle point: rank is not always a measurement

`Poor < Fair < Good < Excellent` gives a sensible order. But code numbers 0, 1, 2, and 3 also place equal-sized gaps between adjacent levels. That may or may not match the real meaning. `OrdinalEncoder` preserves the rank you specify; it cannot tell whether the distance from Poor to Fair is truly the same size as the distance from Good to Excellent.

For now, remember: **ordinal means ordered**. It does not automatically mean the numbers are measured quantities with precise, equal intervals.

## 8. Is this training data?

The CSV is still a tiny practice dataset, not a dataset for training a prediction model. It has input information but no target column with a correct answer the model should learn to predict.

`OrdinalEncoder.fit_transform(...)` does not contradict that. Encoders and predictive models both have methods named `fit`, but they fit different things. Here, the transformer applies a category-to-number rule. Later, when we train a predictive model, we will identify its features and target, split data carefully, and measure performance separately.

The sample is also far too small and invented to support claims about real product reviews. It only demonstrates how encodings behave.

## 9. Try two changes

1. Change the order of `condition_order`, then run the script. Which condition codes change? Why do the manual dictionary and `OrdinalEncoder` still agree?
2. Change the order of `department_order`, then run again. The ordinal department codes will change, while the `dept_...` one-hot flags still identify the same department. What does that tell you about whether department order has meaning?

## 10. Words to keep

- **Nominal category:** a group label with no inherent ranking, such as department name.
- **Ordinal category:** a group label with a meaningful order, such as a condition scale.
- **One-hot encoding:** one 0/1 column per category.
- **Ordinal encoding:** integer codes assigned according to a category order.
- **Transformer:** a tool that changes input data into another representation.
- **`fit_transform`:** set up a transformation from data/configuration and apply it to that data.
- **Target:** the answer a supervised model is trained to predict; this practice dataset has none.

## 11. How this fits the learning path

Lesson 1 turned one unordered category column into one-hot flags. Today we compared that with ordered integer codes and connected the encoder to the dictionary mapping you already know. A later lesson can look at multiple numeric and category columns together, then we can gradually move toward train/evaluation splits and a first simple model.

For current API details, consult the scikit-learn user guide section on encoding categorical features and the `OrdinalEncoder` API reference.
