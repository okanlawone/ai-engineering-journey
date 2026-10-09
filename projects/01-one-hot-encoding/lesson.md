# Lesson 1 — One category, several 0/1 columns

**Today’s goal:** Understand the exact behavior of `pd.get_dummies()` and why the variable called `one_hot` does not become one single column in `reviews`.

**Pace:** One idea at a time. Today we only prepare a category column. We do not fit a model.

## 1. The little table we start with

Open `data/reviews.csv`. It has ten rows. Each row has a review ID and the department the review belongs to. These are small, invented practice rows so we can see the transformation clearly; they are not from your store or real customer reviews.

A **row** is one record. A **column** is one kind of information recorded for every row. Here, `department_name` is a column, and values such as `Bottoms` and `Dresses` are its **categories**.

Some values repeat. That is useful: the program should give every review in `Bottoms` the same `dept_Bottoms` flag.

## 2. Why turn words into numbers?

People can read `Bottoms` directly. Many machine-learning algorithms work with numeric input, so before a later model can use this information, we often convert it into numbers in a way that preserves what the category means.

`department_name` is a **nominal category**: the names identify groups, but one department is not inherently greater or smaller than another. Giving `Bottoms` the number 0, `Dresses` 1, and `Intimate` 2 can accidentally suggest an order. **One-hot encoding** avoids that suggestion by giving each category its own flag column.

## 3. What `get_dummies()` returns

The central line is:

```python
one_hot = pd.get_dummies(
    reviews["department_name"],
    prefix="dept",
    dtype=int,
)
```

Read it from the inside outward:

1. `reviews["department_name"]` selects just that column from the DataFrame. The result is a pandas Series: one list-like column of values.
2. `pd.get_dummies(...)` looks at the distinct category values in that Series.
3. It builds a **new DataFrame** with one column for each distinct category.
4. In each row, the matching category gets `1`; the other department columns get `0`.
5. `prefix="dept"` adds `dept_` to the new column names, so the categories are easy to recognize.
6. `dtype=int` makes the flags display as whole-number `0` and `1` values.

For the first row, whose department is `Bottoms`, the result is conceptually:

| dept_Bottoms | dept_Dresses | dept_Intimate | dept_Jackets | dept_Tops | dept_Trend |
|---:|---:|---:|---:|---:|---:|
| 1 | 0 | 0 | 0 | 0 | 0 |

The variable name `one_hot` is just the name you gave to the **whole new DataFrame**. It does not create a column named `one_hot`. Its columns are named after the categories (plus the prefix).

## 4. What `join()` does

```python
reviews = reviews.join(one_hot)
```

`join()` attaches the new columns to the original `reviews` DataFrame. By default, pandas lines rows up by their index. Both tables came from the same CSV and still have matching indexes, so each row receives flags for its own department.

The assignment back to `reviews` matters: it makes the name `reviews` refer to the combined DataFrame. The original `department_name` column stays there too. `join()` adds columns; it does not remove the source column.

After the join, the columns are:

```text
review_id, department_name, dept_Bottoms, dept_Dresses,
dept_Intimate, dept_Jackets, dept_Tops, dept_Trend
```

That is why printing `reviews.columns` does not show a single `one_hot` column. Look for names beginning with `dept_` instead. Without `prefix="dept"`, the columns would simply be named `Bottoms`, `Dresses`, `Intimate`, and so on.

## 5. Walk through `main.py`

### Find and load the data

```python
from pathlib import Path
import pandas as pd

data_path = Path(__file__).parent / "data" / "reviews.csv"
reviews = pd.read_csv(data_path)
```

- `Path` helps build a file location that works across folders and operating systems.
- `__file__` means “the location of this Python file.”
- `Path(__file__).parent` is the project folder.
- The next pieces point into `data/reviews.csv`.
- `pd.read_csv(...)` reads the CSV into a pandas DataFrame called `reviews`.

The other print statements let us see three stages: the original table, the new one-hot table by itself, and both tables joined together. Printing `one_hot` separately is a handy way to inspect what the transformation made before combining it.

## 6. Is this training data?

The CSV is a **dataset** for this lesson. In this project it is practice data for learning a transformation. We have not trained a model.

For a typical **supervised-learning** task, training data contains examples and the correct answer the model is meant to learn to predict. For example, a future review project might use review information as **features** (the inputs) and a human-provided sentiment label as the **target** (the answer). This CSV has department names, but no sentiment target, so it cannot teach a supervised model to predict sentiment.

When we later train a model, we will slow down and look at the target, how rows are split into training and evaluation groups, and how to tell whether a model learned a useful pattern. Those steps come later. Today we only make a category usable as numeric feature columns.

A model dataset also needs careful thought about where its rows came from, whether labels are trustworthy, whether private information is present, and whether the examples represent the situation where the model will be used. We will discuss those questions when a project actually uses model training data.

## 7. Run it and inspect the result

From this folder, run:

```bash
python main.py
```

First, confirm that the standalone one-hot table has six department columns. Then confirm that the combined table has the original two columns plus those six new columns. In every row, exactly one of the six department flags should be `1`, because every practice row has one department.

## 8. Small exercise

Change one row in `data/reviews.csv` from `Tops` to `Shoes`, run the program again, and look at the column list. What new column appeared? Why does the `Shoes` row have a `1` there?

Then remove `prefix="dept"` and run it again. How did the generated column names change? The underlying category flags still work the same way.

## 9. Words to keep

- **Category:** a named group such as `Dresses`.
- **DataFrame:** a labeled table of rows and columns in pandas.
- **Feature:** information used as an input to a model.
- **One-hot encoding:** a conversion that gives each category its own 0/1 column.
- **Dataset:** a collection of data records; it is not automatically model-training data.
- **Training data:** examples used to teach a model. In supervised learning, these examples include the correct target answer.
- **Target / label:** the answer a supervised model is trained to predict.

## 10. Where the course goes next

We will move in small steps, and pause to explain new words before relying on them:

1. **Python and tables:** variables, lists, dictionaries, functions, rows, columns, and missing values.
2. **Preparing data:** category encoding, numeric columns, text basics, and checking data quality.
3. **First classic models:** a simple prediction task, features and target, training versus evaluation data, and a baseline.
4. **Understanding performance:** appropriate metrics, errors, overfitting, and why a tiny practice dataset cannot prove real-world accuracy.
5. **More capable models:** decision trees, ensembles, and careful comparisons.
6. **Text and neural networks:** represent text, build a small neural network, and understand training at a high level before adding complexity.
7. **Modern AI projects:** embeddings, language models, retrieval, evaluation, privacy, and a small deployed project.

Each stage will grow from the previous one. We will keep toy data clearly labeled, explain what every important line does, and only claim measured results when we actually calculate them.
