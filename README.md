# AI Engineering Journey

I'm Tomi, a CIT graduate and founder who ships, building toward AI engineering and product roles through hands-on projects.

This repository documents a slow, honest progression from beginner foundations toward advanced AI and machine learning work. Each numbered project is runnable on its own and includes a lesson that explains the code and the choices behind it.

## Projects

| Project | Concept | What it demonstrates | Materials |
| --- | --- | --- | --- |
| 01 · One-hot encoding | Represent unordered department categories as indicator columns | Use pandas to create one-hot columns and join them back to the original reviews table | [Project guide](projects/01-one-hot-encoding/README.md) · [Lesson](projects/01-one-hot-encoding/lesson.md) |
| 02 · Ordinal encoding | Choose encodings based on whether categories have a meaningful order | Compare one-hot encoding for department names with a manual mapping and scikit-learn's `OrdinalEncoder` for product condition | [Project guide](projects/02-ordinal-encoding/README.md) · [Lesson](projects/02-ordinal-encoding/lesson.md) |

**Skills so far:** Python, pandas, and scikit-learn preprocessing, including categorical encoding.

## Run a project

Install Python 3, clone the repository, and move into the project folder you want to run. For example:

```bash
git clone https://github.com/okanlawone/ai-engineering-journey.git
cd ai-engineering-journey/projects/01-one-hot-encoding
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

To run another project, replace `01-one-hot-encoding` in the `cd` path with that project's folder name. Each project has its own `requirements.txt` and `main.py`.

## Data and scope

The first two projects use small, invented practice datasets made to explain preprocessing. They do not contain real customer data. These projects prepare columns; they do not train prediction models yet.

## Roadmap

- Train and inspect a first prediction model.
- Explore unsupervised learning with K-means clustering.
- Evaluate results with suitable metrics and clear comparisons.
