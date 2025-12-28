
import requests
import pandas as pd

url ="https://dumps.wikimedia.org/other/pageviews/2025/2025-12/pageviews-20251226-090000.gz"

filename = 'projectviews-20251226-090000'

response = requests.get(url) 
with open(filename, "wb") as f: 
    f.write(response.content)
    
""" Read with pandas """
df = pd.read_csv(filename, compression="gzip", sep=" ",
                 header=None, names=["project", "page_title", "views", "bytes"])

"Normalize page titles (replace underscores with spaces)"
df["page_title"] = df["page_title"].str.replace("_", " ")

"""Define companies of interest"""
companies = ["Apple", "Amazon", "Facebook", "Google", 
                "Microsoft", "Tesla", "IBM", "Oracle"]

"""Filter rows where page_title matches one of the companies"""
company_views = df[df["page_title"].isin(companies)][["page_title", "views"]] 

# summary = company_views.groupby("page_title")["views"].sum().reset_index()

print(company_views)

