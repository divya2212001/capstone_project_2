# Capstone 2 — Finance (LendingClub)

## Executive Summary
We analyzed LendingClub loan-level records to understand default-risk drivers and translate them into underwriting and portfolio actions. The project includes a Python ETL pipeline, EDA, statistical modeling, and Tableau-ready extracts.

**Dataset**: Lending Club Loan Data CSV (raw from Kaggle)
- Raw file: `data/raw/loan.csv`
- Cleaned file: `data/processed/clean_lendingclub.csv`
- Tableau extracts: `data/processed/tableau_loans.csv`, `data/processed/kpi_summary.csv`

## Problem Statement
**Goal**: Identify the main drivers of loan default risk and propose changes in underwriting/portfolio mix to reduce expected defaults while maintaining revenue.

## Data Description
- Rows (raw loans): 2,260,668
- Core target proxy: `is_default` derived from `loan_status`
- Key fields used: loan amount, interest rate, term, grade/sub-grade, DTI, income, purpose, verification status, state, issue date.

## ETL Methodology (Python)
Cleaning and standardization steps (implemented in the cleaned dataset):
- Standardized column naming
- Parsed `issue_d` into `issue_date`, `issue_year`, `issue_month`
- Normalized categorical fields (trim/standardize)
- Derived `term_months` and `emp_length_years`
- Derived binary label `is_default` from adverse `loan_status` states

## KPI Framework
- **Default rate**: defaults / loans
- **Exposure proxy**: sum of loan amount
- **Pricing**: average interest rate

Overall KPIs (cleaned dataset):
- Default rate: 0.1258
- Avg interest rate: 13.09
- Avg loan amount: 15046.93

## EDA Highlights
(See figures in `reports/figures/`.)

1. **Default rate trend over time** (Figure: `default_rate_trend.png`)
2. **Default rate by grade** (Figure: `default_rate_by_grade.png`)
3. **Default rate by purpose** (Figure: `default_rate_by_purpose_top12.png`)

## Statistical Analysis
We trained a baseline **logistic regression** model to predict `is_default` using numeric and categorical borrower/loan features with imputation + one-hot encoding.

Model performance (held-out test set):
- ROC-AUC: 0.680
- Avg Precision: 0.389

Top drivers (by coefficient magnitude) are provided in: `reports/model_top_coefficients.csv`.

## Key Insights (write 8–12 in decision language)
Use these as placeholders and refine after reviewing the EDA tables and model coefficients:
1. Default risk varies strongly by **grade/sub-grade**, indicating underwriting buckets are decision-critical.
2. Longer terms (60 months) typically carry higher risk than 36-month terms.
3. Certain **purposes** concentrate higher default risk; portfolio mix can reduce expected defaults.
4. Higher **DTI** is associated with increased default risk.
5. Verification status segments show different risk profiles.
6. Geography shows meaningful variation; it can guide targeted policy or monitoring.
8. Missingness patterns may correlate with risk and should be handled consistently.
9. Interest rate is correlated with risk; pricing alone may not compensate for risk in some segments.
10. A small subset of segments drives a large share of expected defaults (Pareto effect).

## Recommendations (3–5, with impact estimation)
1. **Tighten policy for high-risk grade+term combinations** (e.g., restrict 60-month for weaker grades) and estimate reduction in expected defaults using segment default rates.
2. **Add DTI-based guardrails**: enforce thresholds/bands and require additional verification above a DTI cutoff.
3. **Rebalance portfolio mix** away from highest-default purposes toward lower-risk purposes where revenue impact is minimal.
4. **Monitoring dashboard**: track default rate and volume monthly by grade/purpose/state; alert on drift.
5. **Improve data capture for high-missingness fields** if missingness correlates with risk (reduce uncertainty and improve decisions).

## Tableau Dashboard
- Dashboard link: add to `tableau/dashboard_links.md` after publishing
- Required filters: year/date, grade/sub-grade, term, purpose, state
- Use `data/processed/tableau_loans.csv` and/or `data/processed/kpi_summary.csv` as sources

## Limitations & Future Scope
- `is_default` is derived from `loan_status` and may mix late/default states; refine the label definition if needed.
- This analysis is observational; causal impact needs controlled policy tests.
- Future work: more robust models (tree-based), calibration, and profit/expected loss modeling.

## Contribution Matrix
Fill using `docs/team_contribution_plan.md` and match GitHub Insights/PR history.
