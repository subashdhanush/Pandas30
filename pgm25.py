import pandas as pd

df=pd.read_csv('data.csv')
x=df["calories"].median()
df.fillna({"calories":x},inplace=True)
print(df.to_string())