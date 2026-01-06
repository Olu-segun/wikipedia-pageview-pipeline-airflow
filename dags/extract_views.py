import requests
import pandas as pd
from dotenv import load_dotenv
import os
import gzip

load_dotenv()

FILENAME = "/opt/airflow/view_data/pageviews-20251226-090000.csv"
LOCAL_GZ = "/opt/airflow/view_data/pageviews-20251226-090000.gz"

def extract_company_views():
    url = os.getenv("wikipedia_page_view_url")
    if not url:
        raise ValueError("Environment variable 'wikipedia_page_view_url' is not set")

    target_companies = {"Apple", "Amazon", "Facebook", "Google", "Microsoft", "Tesla", "IBM", "Oracle"}

    try:
        os.makedirs(os.path.dirname(LOCAL_GZ), exist_ok=True)
        os.makedirs(os.path.dirname(FILENAME), exist_ok=True)

        # Download dump file
        print(f"Downloading dump file from {url}...")
        with requests.get(url, stream=True, timeout=300) as r:
            r.raise_for_status()
            with open(LOCAL_GZ, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        print("Download complete.")

        # Parse gzip and filter
        filtered_data = []
        with gzip.open(LOCAL_GZ, "rt", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(" ")
                if len(parts) >= 3:
                    project, page_title, views = parts[0], parts[1], parts[2]
                    if page_title in target_companies:
                        filtered_data.append({
                            "project": project,
                            "page_title": page_title,
                            "views": int(views)
                        })

        df = pd.DataFrame(filtered_data)
        df.to_csv(FILENAME, index=False)
        print(f"Saved {len(df)} rows to {FILENAME}")
        return FILENAME

    except Exception as e:
        raise RuntimeError(f"Error extracting wikipedia page views: {e}")
