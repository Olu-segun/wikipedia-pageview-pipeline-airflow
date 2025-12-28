import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

FILENAME = 'projectviews-20251226-090000.gz'

def extract_company_views():
        try:
            url = os.getenv("wikipedia_page_view_url")
            response = requests.get(url)
            
            if response.status_code != 200:
                raise Exception(f"Bad status code: {response.status_code}")
            
            if not response.text.strip():
                raise Exception(f"Empty response from the url")
            
            with open(FILENAME, "wb") as f:
                f.write(response.content)
                
                """Read with pandas dataframe"""
                df = pd.read_csv(FILENAME, compression="gzip", sep=" ", 
                                 header=None, names=["project", "page_title", "views", "bytes"])
                
            return df
            
        except Exception as e:
            print(f"Error extracting wikipedia page reviews: {e}")

