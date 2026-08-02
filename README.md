# Patient Readmission Risk & Hospital Operations Analytics

Healthcare analytics project that analyzes patient readmission patterns using **Excel**, **PostgreSQL**, and **Power BI** to identify factors associated with 30-day hospital readmissions and support data-driven healthcare decisions.

---

## Project Overview

Hospital readmissions increase healthcare costs and may indicate gaps in patient care. This project analyzes patient records to identify trends related to readmission risk and presents insights through interactive dashboards and SQL analysis.

**Business Question**

> Which patient and operational factors are associated with 30-day readmission, and how can healthcare providers use these insights to improve patient outcomes?

---

## Tools Used

| Tool | Purpose |
|------|---------|
| **Excel** | Data cleaning with Power Query, PivotTables, Pivot Charts, KPI dashboard, and slicers |
| **PostgreSQL** | Database design, data storage, and analytical SQL queries |
| **Power BI** | Interactive dashboard creation, data modeling, DAX measures, and KPI reporting |

---

## Project Workflow

```text
Raw Patient Data
        │
        ▼
Excel (Power Query Cleaning)
        │
        ▼
Cleaned Dataset
        │
 ┌──────┴──────┐
 ▼             ▼
PostgreSQL   Power BI
(SQL)        Dashboard
        │
        ▼
Business Insights
```

---

## Project Features

### Excel

- Data cleaning using Power Query
- PivotTables for patient analysis
- Interactive Pivot Charts
- KPI dashboard
- Slicers for filtering data
- Summary statistics

### PostgreSQL

- Normalized healthcare database
- SQL analysis queries
- Aggregate functions
- Joins
- Common Table Expressions (CTEs)
- Window functions

### Power BI

- Interactive dashboard
- KPI cards
- DAX measures
- Slicers and filters
- Trend visualizations
- Readmission analysis

---

## Repository Structure

```text
Patient-Readmission-Analytics/
│
├── data/
│   ├── Raw_Patient_Data.csv
│   └── Cleaned_Patient_Data.csv
│
├── excel/
│   └── Patient_Readmission_Dashboard.xlsx
│
├── sql/
│   ├── postgresql_schema.sql
│   └── analysis_queries.sql
│
├── powerbi/
│   ├── Patient_Readmission_Dashboard.pbix
│   
│
└── README.md
```

---

## Dashboard Highlights

The Power BI dashboard includes:

- Total Patients
- Readmission Rate
- Average Length of Stay
- Readmission by Department
- Readmission by Chronic Condition
- Follow-up Appointment Analysis
- Discharge Disposition Analysis
- Interactive filters and slicers

---

## Excel Dashboard Highlights

- KPI Cards
- PivotTables
- Pivot Charts
- Department Analysis
- Chronic Condition Analysis
- Follow-up Analysis
- Discharge Disposition Analysis

---

## SQL Analysis

The SQL scripts include analyses such as:

- Readmission rate by department
- Chronic condition impact on readmission
- Follow-up appointment analysis
- Average length of stay
- Prior admissions analysis
- Discharge disposition trends
- Patient summary statistics

---

## Key Insights

- Patients with chronic conditions experience higher readmission rates.
- Patients without scheduled follow-up appointments are more likely to be readmitted.
- Longer hospital stays are associated with higher readmission risk.
- Readmission trends vary across discharge dispositions and patient characteristics.

---

## Skills Demonstrated

### Excel

- Power Query
- PivotTables
- Pivot Charts
- Slicers
- Dashboard Design
- Data Cleaning

### PostgreSQL

- Database Design
- SQL Queries
- Joins
- CTEs
- Window Functions
- Aggregate Functions

### Power BI

- Data Modeling
- DAX
- Interactive Dashboards
- KPI Cards
- Slicers
- Data Visualization

---

