## Project Description

This project implements an Apache Airflow DAG to automate the extraction and analysis of Wikipedia pageview data. Specifically, it tracks hourly pageview trends for the "Big Five" tech companies: Amazon, Apple, Facebook, Google, and Microsoft.

---
## Tech Stack

• Orchestrator: Apache Airflow (DAGs)

• Database: PostgreSQL

• Language: Python 3.11
 
---
 ## Project Workflow
 
1.	Extract: Download and unzip Wikipedia pageview data for a specific hour in December 2025.

2.	Transform: Filter the dataset to isolate the five targeted companies and extract pageview counts.

3.	Load: Insert the processed data into a PostgreSQL database.

4.	Analyze: Execute a SQL query to identify the company with the highest engagement.
--
