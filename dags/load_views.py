import pandas as pd
from airflow.providers.postgres.hooks.postgres import PostgresHook

def load_company_views(filepath: str):
    try:
       
        df = pd.read_csv(filepath)

        
        records = list(df.itertuples(index=False, name=None))

        
        postgres_hook = PostgresHook(postgres_conn_id="wikipedia_page_view")
        conn = postgres_hook.get_conn()
        cur = conn.cursor()

        
        cur.execute("""
            CREATE TABLE IF NOT EXISTS wikipedia (
                id SERIAL PRIMARY KEY,
                page_title VARCHAR(100) UNIQUE,
                views INTEGER
            )
        """)

        """Clear old data to avoid duplicates"""
        cur.execute("TRUNCATE TABLE wikipedia RESTART IDENTITY;")

        
        insert_query = "INSERT INTO wikipedia (page_title, views) VALUES (%s, %s)"
        cur.executemany(insert_query, records)

        conn.commit()
        print(f"✅ Successfully inserted {len(records)} records into Postgres.")

        cur.close()
        conn.close()

    except Exception as e:
        print(f"❌ Database error: {e}")
        if 'conn' in locals() and conn:
            conn.rollback()
            conn.close()
