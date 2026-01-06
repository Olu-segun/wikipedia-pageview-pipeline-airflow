# 📊 Wikipedia Pageview Data Pipeline (Apache Airflow)
## 📌 Project Description

This project implements an Apache Airflow–orchestrated ETL pipeline to automate the extraction, transformation, and loading of Wikipedia pageview data.
The pipeline tracks hourly pageview activity for selected global technology companies — Apple, Amazon, Facebook, Google, Microsoft, Tesla, IBM, and Oracle — and stores the processed results in a PostgreSQL database for analysis.

The goal of this project is to demonstrate end-to-end data pipeline development, including data ingestion from external sources, transformation logic, database loading, and analytical querying.

---

## 🛠️ Tech Stack

-	Orchestration: Apache Airflow

-	Programming Language: Python 3.11

-	Database: PostgreSQL

-	Data Processing: Pandas

-   Infrastructure: Docker & Docker Compose

-	Data Source: Wikimedia Pageviews Dumps
---
 ## Project Workflow
 
1.	Extract

    •   Downloads hourly Wikipedia pageview data (compressed .gz format) for a specified hour in December 2025.

    •    Stores the raw file locally for processing.

2. Transform

    •   Decompresses and parses the dataset.

    •   Filters records to include only predefined companies of interest.

    •  Aggregates total pageviews per company.

3. Load

    •   Inserts the transformed dataset into a PostgreSQL table.

    •   Ensures the target table exists before loading.

4. Analyze

    •  Runs SQL queries to identify engagement trends.

    •  Determines the company with the highest pageview count for the selected time window
---
### 📁 Repository Structure
<pre>
Wikipedia-Pageview-Data-Pipeline/
│
├── dags/
│   ├── wikipedia_company_views_etl_pipeline.py   # Main Airflow DAG
│   ├── extract_views.py                          # Data extraction logic
│   ├── transform_views.py                        # Data transformation logic
│   ├── load_views.py                             # Data loading logic
│
├── pyenv/                                        # Python virtual environment
├── logs/                                         # Airflow task logs
├── docker-compose.yaml                           # Airflow & Postgres services
├── requirements.txt                              # Python dependencies
└── README.md
</pre>
---
## 📈 Logs & Execution Evidence
The following screenshots demonstrate successful pipeline execution and data validation:

### Airflow DAG Run:
<p align= "center" > 
    <img src="images/airflow_ui_run.jpeg" width="800"> 
</p>

### PostgreSQL Query Results:
<p align= "center" > 
    <img src="images/query_run.jpeg" width="800"> 
</p>
        
---
## 🚀 Key Highlights

-   End-to-end ETL pipeline using Apache Airflow

-   Real-world external data ingestion (Wikimedia dumps)

-   Modular, reusable Python code structure

-   PostgreSQL-based analytical storage

-   Dockerized environment for easy setup and reproducibility
---
## 🎯 Use Cases

-   Monitoring public interest trends for major technology companies

-   Demonstrating data engineering and analytics engineering skills
