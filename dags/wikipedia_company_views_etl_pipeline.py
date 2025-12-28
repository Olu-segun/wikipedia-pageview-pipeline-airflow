from extract_views import extract_company_views
from transform_views import transform_company_views

def company_views_etl_pipeline():
    raw_views = extract_company_views()   
    transformed_views = transform_company_views(raw_views)
    print(transformed_views)

company_views_etl_pipeline()
