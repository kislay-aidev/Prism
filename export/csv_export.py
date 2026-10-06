import pandas as pd
def export(df,path):
    df.to_csv(path,index=True)
    return path
