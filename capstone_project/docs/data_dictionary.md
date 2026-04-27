# Data Dictionary

## Dataset Overview
- **Dataset name**: Lending Club Loan Data (CSV)
- **Source URL**: `https://www.kaggle.com/datasets/adarshsng/lending-club-loan-data-csv/data`
- **Backup A URL**: `https://www.kaggle.com/datasets/wordsforthewise/lending-club/`
- **Backup B URL** (alt dataset, same sector): `https://www.kaggle.com/datasets/iuriivoloshyn/cfpb-consumer-complaint-database/code`
- **Download date**: 2026-04-27
- **Raw file name** (stored in `data/raw/`): `loan.csv`
- **Row count (raw)**: 2,260,668
- **Column count (raw)**: 145
- **Unit of analysis** (what 1 row represents): One loan application/loan record (loan-level)
- **Grain** (unique key or identifying fields): `id` (loan identifier); duplicates should be checked during ETL

## Column-Level Dictionary
Fill this for the columns you will actually use in analysis and Tableau (start with these common LendingClub fields, then adjust to match your downloaded file schema).

- **loan_status**
  - **type**: categorical
  - **description**: Outcome/state of the loan (used to derive default/non-default labels)
  - **example values**: Fully Paid, Charged Off, Current, Late (31-120 days)
  - **cleaning rules applied**: standardize casing/whitespace; define a binary `is_default` mapping for analysis

- **issue_d** (or similar “issue date” field)
  - **type**: datetime
  - **description**: Loan issue date (used for cohort/time trend analysis)
  - **cleaning rules applied**: parse to date; create `issue_year`, `issue_month`

- **int_rate**
  - **type**: numeric
  - **description**: Interest rate (often stored as a percent string)
  - **cleaning rules applied**: strip `%`, convert to float; validate range

- **term**
  - **type**: categorical
  - **description**: Loan term length
  - **example values**: 36 months, 60 months
  - **cleaning rules applied**: normalize text; extract numeric months

- **grade / sub_grade**
  - **type**: categorical
  - **description**: LendingClub credit grade buckets
  - **cleaning rules applied**: normalize categories; use ordering for analysis

- **loan_amnt**
  - **type**: numeric
  - **description**: Principal amount funded/requested
  - **cleaning rules applied**: ensure numeric; handle outliers via winsorization/capping rule (document)

- **annual_inc**
  - **type**: numeric
  - **description**: Borrower annual income
  - **cleaning rules applied**: numeric; handle missing values; consider log transform for modeling

- **dti**
  - **type**: numeric
  - **description**: Debt-to-income ratio
  - **cleaning rules applied**: numeric; cap unrealistic values; handle missing

- **purpose**
  - **type**: categorical
  - **description**: Stated loan purpose
  - **cleaning rules applied**: normalize categories; group rare categories into “Other”

- **addr_state**
  - **type**: categorical
  - **description**: Borrower state (for regional analysis)
  - **cleaning rules applied**: normalize; validate against known state codes

- **emp_length**
  - **type**: categorical/ordinal
  - **description**: Employment length (often stored as text)
  - **cleaning rules applied**: normalize text; map to ordinal years; handle “< 1 year”, “10+ years”

## Data Quality Notes (Raw)
- **Missing values**: expected across income, employment length/title, DTI, and other borrower attributes (confirm after download)
- **Inconsistent formats**: percent strings (interest rate), date strings (issue date), mixed text formats (employment length)
- **Duplicates**: check for duplicate loan IDs/rows (confirm after download)
- **Outliers**: income, DTI, loan amount, revolving utilization can contain extreme values
- **Known limitations**: observational data; default definition depends on `loan_status` mapping

## Derived Fields / KPIs (Processed)
Start with these KPIs/derived fields (finalize after schema confirmation):

- **is_default**: binary label derived from `loan_status` (document mapping)
- **default_rate**: \(\frac{\#\ \text{defaults}}{\#\ \text{loans}}\) by segment/time
- **avg_interest_rate**: average `int_rate` by segment
- **portfolio_mix**: share of loans by grade/purpose/term over time
- **risk_band**: bucketed risk segments (e.g., by grade/DTI/income quantiles)

