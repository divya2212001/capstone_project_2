## Capstone 2 — Data Visualization & Analytics

This repository contains an end-to-end, industry-style data analytics project using:
- **Python** for ETL, cleaning, analysis
- **Tableau** for dashboarding and storytelling
- **GitHub** for version control and collaboration

## Sector & Problem Statement
- **Sector**: Finance (Lending)
- **Problem statement**: Identify the key drivers of **loan default risk** and quantify how changes in underwriting/portfolio mix could reduce expected defaults while maintaining revenue.

## Dataset
- **Primary dataset (Kaggle)**: `https://www.kaggle.com/datasets/adarshsng/lending-club-loan-data-csv/data`
- **Backup A (Kaggle alt LendingClub)**: `https://www.kaggle.com/datasets/wordsforthewise/lending-club/`
- **Backup B (Kaggle, complaints)**: `https://www.kaggle.com/datasets/iuriivoloshyn/cfpb-consumer-complaint-database/code`
- **Meets requirements**: \( \ge 5{,}000 \) rows, \( \ge 8 \) meaningful columns, raw/unprocessed, requires real cleaning

## Repo Structure
- `data/raw/`: Original, unedited dataset (commit as-is; never overwrite)
- `data/processed/`: Cleaned/standardized dataset outputs
- `notebooks/`: Jupyter notebooks (ETL, EDA, statistical analysis, final load prep)
- `scripts/`: Reusable Python scripts (ETL pipeline)
- `tableau/`: Dashboard artifacts (screenshots + published link)
- `docs/`: Data dictionary and documentation
- `reports/`: Final report and presentation PDFs

## Notebooks (Expected)
- `notebooks/01_extraction.ipynb`
- `notebooks/02_cleaning.ipynb`
- `notebooks/03_eda.ipynb`
- `notebooks/04_statistical_analysis.ipynb`
- `notebooks/05_final_load_prep.ipynb`

## How to Run (Local)
1. Add the raw dataset file(s) to `data/raw/`
2. Run notebooks in order from `01_...` to `05_...`
3. Export the final Tableau-ready dataset to `data/processed/` (or a dedicated output in `data/processed/`)

## Tableau
- Published dashboard URL: see `tableau/dashboard_links.md`

## Team & Contributions
- Maintain a PR-based workflow; ensure every member has visible commits/PRs.
- Contribution matrix: include in the final report and keep aligned with GitHub history.

