# P01 ⭐ — Healthcare SQL
## The Darko Method 2026 | Student Project

---

## Your Brief

**Company:** MedCore Analytics
**Client:** St. Aurelius General Hospital
**Your role:** Data Analyst

St. Aurelius General Hospital stores all operational data in PostgreSQL. The Head of
Finance needs a raw data extract that combines patient records, appointment history,
and billing information into one flat file for the analytics team.

Your job is to connect to the Supabase database, write SQL queries against the
`healthcare` schema, and produce `raw-data.csv`.

**Schema:** `healthcare`
**Key tables:** `patients`, `appointments`, `billing`, `doctors`, `departments`

**Deliverable:** `data/raw-data.csv` — a joined extract combining patient, appointment,
and billing data, ready for Module 05 ETL.

---

## Success Criteria

- [ ] You can run individual queries against the healthcare schema in DBeaver
- [ ] Your SQL files cover: basics, aggregation, joins, and at least one CTE or window function
- [ ] `python run.py` connects to the database and saves `raw-data.csv`
- [ ] The CSV contains columns from at least two joined tables
- [ ] Your project is version controlled and pushed to GitHub

---

> Build your project from scratch using the teaching project as your reference.
> Your SQL files go in a `sql/` folder — same structure as the teaching project.
