# NLP_Mozambican_Project
# Improving Machine Translation for Mozambican Portuguese

## Overview

This project investigates how machine translation (MT) systems handle **Mozambican Portuguese**, focusing on two specific sources of linguistic variation:

- **Informal orthography** (e.g., abbreviations, phonetic spelling, non-standard forms)
- **Borrowed vocabulary** from local languages (e.g., Bantu-origin terms)

We test whether a simple **rule-based normalization step** applied before translation can improve MT output quality.

---

## Research Question

How do informal orthography and borrowed vocabulary affect machine translation quality for Mozambican Portuguese, and can lightweight normalization improve translation accuracy?

---

## Approach

We implement a small, reproducible pipeline:

1. **Data collection**
   - ~100 Mozambican Portuguese sentences curated from AfriSenti and public online sources
   - Each sentence is manually annotated with:
     - `phenomenon` (informal_orthography or borrowed_vocab)
     - `key_token` (target word(s))

2. **Baseline translation**
   - Sentences are translated using an existing MT system (e.g., Google Translate)

3. **Normalization**
   - A rule-based system is applied:
     - **Orthography rules** (e.g., `pq → porque`, `Vamu → Vamos`)
     - **Lexicon for borrowed terms** (e.g., marking or mapping local words)

4. **Re-translation**
   - Normalized sentences are translated using the same MT system

5. **Evaluation**
   - Compare baseline vs normalized translations
   - Qualitative error analysis
   - Simple counts of improvements by category

---
## Repository Structure


data/
raw/ # original sentences
processed/ # normalized sentences

rules/
orthography_rules.json
lexicon.json

src/
normalize.py
evaluate.py

results/
baseline_translations.csv
normalized_translations.csv
evaluation.csv

## Preliminary Observations

- MT systems struggle with **informal abbreviations and spelling variation**
- Normalization often improves fluency and lexical accuracy
- **Borrowed vocabulary remains challenging**, even after normalization

---

## Limitations

- Small dataset (~100 sentences)
- Manual annotation and evaluation
- Rule-based normalization is limited in coverage
## Reproducibility

All data (or pointers), normalization rules, and scripts are included to allow replication and extension of this work.

---

## Next Steps

- Expand borrowed vocabulary lexicon
- Refine normalization rules
- Analyze error patterns in more detail