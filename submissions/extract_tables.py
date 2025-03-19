

def extract_tables(path: str):
    import tabula
    import pandas as pd

    if not path.endswith(".pdf"):
        return ValueError
    
    df = pd.DataFrame(None, columns=["Page", "Maths", "Physics", "English", "Economics", "Biology"])
    
    for i in range(1, 101):
        dfs = tabula.read_pdf(path, pages = i)
        dfs = dfs[0]
        dfs["Page"] = i
        df = pd.concat([df, dfs], ignore_index=True)
    
    students = df[(df["Economics"] >= 45) & (df["Page"] >= 44) & (df["Page"] <= 73)]
    
    results = students["Maths"].sum()
    
    return str(results)
    