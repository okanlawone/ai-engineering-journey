# AI Engineering Journey

I’m Tomi, a CIT graduate and founder building toward AI engineering and product roles through hands-on projects. This repository documents a slow, honest progression from beginner foundations toward advanced AI and machine-learning work.

## Project index

Each project now lives in its own standalone repository. That repository is the canonical home for its runnable code, detailed teaching guide, open-ended challenge, and multi-session progress tracker.

| Project | Concept | Standalone repository |
| --- | --- | --- |
| 01 | One-hot encode unordered department categories with pandas | [01-one-hot-encoding](https://github.com/okanlawone/01-one-hot-encoding) |
| 02 | Compare nominal one-hot features with meaningful ordinal codes | [02-ordinal-encoding](https://github.com/okanlawone/02-ordinal-encoding) |
| 03 | Select numeric features and scale without fitting preprocessing on held-out rows | [03-scaling-numeric-features](https://github.com/okanlawone/03-scaling-numeric-features) |
| 04 | Retrieve source passages for document questions and inspect evidence | [04-document-qa-system](https://github.com/okanlawone/04-document-qa-system) |

Each project repository has a `README.md` for its goal and setup, a `lesson.md` for the detailed explanation and project challenge, and a `progress.md` to record work across sessions. Projects may take more than one day; the next project starts after the current required checkpoints are complete.

## Learning sequence and data

The sequence moves gradually from data preparation into retrieval, model use, and evaluation. Projects 1–3 teach preprocessing concepts and do not claim prediction performance. Project 4 begins a retrieval and knowledge-engineering path. Its handbook is invented practice content, not real policy or model-training data. Practice data is not automatically training data: a supervised model needs a target and a deliberate training/evaluation process.

## Preserved project history

The folders `projects/01-one-hot-encoding`, `projects/02-ordinal-encoding`, and `projects/03-scaling-numeric-features` remain here as copies of the original combined-repository sequence. No project files were removed. Continue future project work in the standalone repositories above.

## Roadmap

Project 4 begins a retrieval and knowledge-engineering path from the shared project-ideas article, which lists “Building a Document Q&A System” among its retrieval and knowledge projects. Session 1 built a transparent retrieval baseline. Session 2 compared raw word-count and TF-IDF rankings on seven answerable and three unanswerable invented questions: raw counts put the expected source first for 3/7 answerable questions, TF-IDF for 1/7, and both returned a passage for all 3/3 unanswerable questions. Session 3 added a hand-written evidence-sufficiency gate. On the 13-question set, it returned the expected source quote for 7/7 answerable questions and abstained for 6/6 unanswerable questions. Session 4 kept those clue groups fixed and compared evidence windows on five fresh invented questions: one-sentence windows exactly quoted 2/3 answerable cases and abstained on 2/2 unsupported cases; up-to-two-sentence windows exactly quoted 3/3 answerable cases but produced a relationship false positive on 1/2 unsupported cases. The interactive path now defaults to the one-sentence setting, while the evaluator preserves both comparisons. These are tiny diagnostic sets, not general performance estimates. The clue groups are a manual heuristic, not learned understanding, and no model is trained. Project 4 remains active to investigate relationship-aware evidence checks with a new question set. Next projects will be chosen from the article and matched to Tomi’s current level. Complex projects can span more than one session; each guide is designed to build understanding, experiments, and judgment rather than syntax memorization.
