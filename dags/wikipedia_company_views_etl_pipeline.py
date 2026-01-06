from airflow import DAG
from airflow.decorators import task
from pendulum import datetime

from extract_views import extract_company_views
from transform_views import transform_company_views
from load_views import load_company_views

with DAG(
    dag_id="wikipedia_page_view",
    schedule=None,
    start_date=datetime(2025, 12, 28),
    catchup=False,
    tags=["wikipedia", "etl"]
) as dag:

    @task()
    def extract_views():
        raw_views = extract_company_views()
        if raw_views is None:
            raise ValueError("Extracted data is None. Check extract_company_views()")
        return raw_views

    @task()
    def transform_views(raw_views):
        if raw_views is None:
            raise ValueError("Extract task returned  None")
        transformed_views = transform_company_views(raw_views)
        return transformed_views

    @task()
    def load_views(transformed_views):
        load_company_views(transformed_views)

    # Task dependencies
    raw = extract_views()
    transformed = transform_views(raw)
    load = load_views(transformed)