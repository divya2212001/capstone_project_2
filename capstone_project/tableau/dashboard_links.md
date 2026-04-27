## Tableau Public Dashboard

- **Dashboard URL**: _PASTE_PUBLIC_TABLEAU_URL_HERE_

## Notes
- Include at least one interactive filter.
- Upload screenshots to `tableau/screenshots/`.

## Dashboard design (Finance — Lending defaults)
### Required interactivity (minimum)
- **Filters**: `issue_year` (or date range), `grade` / `sub_grade`, `term`, `purpose`, `addr_state`
- **Parameter** (optional but recommended): choose metric view (Default Rate vs Volume vs Avg Interest Rate)

### Recommended layout (1 dashboard, 4–6 views)
1. **KPI strip**: Total loans, Total exposure (sum loan amount), Default rate, Avg interest rate
2. **Trend**: Default rate over time (monthly or yearly)
3. **Risk segments**: Default rate by grade/sub_grade (bar chart)
4. **Purpose mix**: Default rate (or volume) by purpose
5. **Geography** (if available): Default rate by state (filled map)
6. **Scatter**: Interest rate vs DTI (color by grade, tooltip includes loan amount and default label)

### Screenshot checklist (commit to repo)
- Overall dashboard (full view)
- One screenshot demonstrating an interactive filter in use

