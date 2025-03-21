
def clean_sales(path: str, product: str = "Car", city: str = "Osaka", sales_min: int = 152):
    import pandas as pd
    df = pd.read_csv(path)
    
    total_sales = df[
        (df["_ - city"] == "Osaka") &
        (df["_ - product"] == "Car") &
        (df["_ - sales"].astype(int) >= 152)
    ]
    
    result = total_sales["_ - sales"].astype(int).sum()
    
    return str(result)