def transform_company_views(df):
    companies = ["Apple", "Amazon", "Facebook", "Google", "Microsoft", "Tesla", "IBM", "Oracle"]
    companies_views = df[df["page_title"].isin(companies)][["page_title", "views"]]
    summary = companies_views.groupby("page_title")["views"].sum().reset_index()
    return summary
