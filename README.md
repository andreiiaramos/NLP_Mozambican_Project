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
We test whether a small rule-based normalization system can improve translation quality.
