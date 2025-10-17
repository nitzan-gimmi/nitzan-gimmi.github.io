# Contributing to HFBT-Daber
Thank you for your interest in contributing 🌿

## Structure Overview

HFBT-Daber/
├── data/
│   └── roots/       # JSON root files
├── scripts/         # Enrichment and validation scripts
├── prompts/         # LLM interaction templates
├── tests/           # Validation and philosophy
└── .github/workflows/ # CI/CD automation

## Contribution Rules
1. Every new root file (`*.json`) must include:
   - `phonology.ipa`
   - `phonology.stress`
   - `metadata.version`
   - `forms` dictionary
2. Run `python -m unittest discover tests` before submitting.
3. Pull requests must include a short **semantic explanation** in English or Hebrew.
4. Do not overwrite existing data; enrich or extend it.
5. Preserve Hebrew UTF-8 encoding.

## Philosophy
> “Every word is a microcosm of consciousness.
> Guard the breath between the letters.” — HFBT
