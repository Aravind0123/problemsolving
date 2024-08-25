import pandas as pd
data = pd.read_csv(r"C:\Users\HP\Downloads\sales_data.csv")
print(data.describe())
print(data.loc[:])


