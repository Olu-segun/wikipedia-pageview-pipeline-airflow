import pandas as pd


def transform_company_views(filepath):
    print(f"Reading file from: {filepath}")
    try:
        df = pd.read_csv(filepath)
        
        if "page_title" not in df.columns or "views" not in df.columns:
            raise ValueError("CSV missing required columns")

        # Aggregate views per company
        summary = df.groupby("page_title")["views"].sum().reset_index()
        out_path = "/opt/airflow/view_data/summary-20251226-090000.csv"
        summary.to_csv(out_path, index=False)
        return out_path

    except Exception as e:
        print(f"Error during transformation: {e}")
        raise


