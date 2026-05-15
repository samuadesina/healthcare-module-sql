Healthcare SQL
My Data Journey 2026 | Student Project
🧠 Project Context (In My Words)
For this project, I’m stepping into the role of a Data Analyst working with healthcare data.

The scenario:
MedCore Analytics supports St. Aurelius General Hospital, and the Finance team needs a clean raw data extract that combines:

Patient records
Appointment history
Billing information
All of this lives in a PostgreSQL database.

My job is to:

Connect to the Supabase database
Write structured SQL queries inside the healthcare schema
Join the relevant tables
Generate a clean flat file → raw-data.csv
Prepare it for downstream ETL work
This project is about practicing real-world SQL, joins, structure, and reproducibility — not just writing queries, but building something complete and usable.

🏥 Database Details
Schema: healthcare
Core Tables I’m Working With:

patients
appointments
billing
doctors
departments
Final Deliverable:
data/raw-data.csv — a joined dataset combining patient, appointment, and billing data.

- What Success Looks Like (For Me)
 I can confidently run queries in DBeaver against the healthcare schema
 My SQL covers:
Basic SELECT statements
Aggregations
Joins 
At least one CTE or window function
 python run.py connects to the database successfully
 The script generates data/raw-data.csv
 The CSV contains fields from multiple joined tables
 The project is cleanly structured and pushed to GitHub
- How I’m Structuring This
I’m building this from scratch, using the teaching project only as a guide.

Project structure:

text

project-root/
│
├── sql/              # All SQL queries
├── data/             # Output CSV
├── run.py            # Database connection + export script
└── README.md
 Why This Project Matters To Me
This isn’t just a SQL exercise.

It’s me practicing:

Writing production-style SQL
Structuring a real data project
Connecting Python to PostgreSQL
Exporting clean datasets
Thinking like an analyst, not just a student