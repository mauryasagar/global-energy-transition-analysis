import pandas as pd

# Load the dataset
df = pd.read_csv('data/owid-energy-data.csv')

# Print the columns and the first 5 rows
print(df.columns)
print(df.head())