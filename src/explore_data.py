import pandas as pd

# Load the datasets
df_energy = pd.read_csv('data/owid-energy-data.csv')
df_co2 = pd.read_csv("data/owid-co2-data.csv")

# Merge them on country and year
df = pd.merge(df_energy, df_co2, on=["country", "year"])

# Select columns
cols = ["country", "year", "renewables_share_energy", "co2_per_capita"]
df = df[cols]

# Print the first 5 rows
print(df.head())