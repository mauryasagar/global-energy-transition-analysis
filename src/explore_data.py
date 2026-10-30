import pandas as pd

# Load the datasets
df_energy = pd.read_csv('data/owid-energy-data.csv')
df_co2 = pd.read_csv("data/owid-co2-data.csv")

# Merge them on country and year
df = pd.merge(df_energy, df_co2, on=["country", "iso_code", "year"])

# Select columns
cols = ["country", "iso_code", "year", "renewables_share_energy", "co2_per_capita"]
df = df[cols]

# Drop rows where iso_code is missing (this removes continents/world)
df = df.dropna(subset=["iso_code"])

# Drop rows with missing values
df = df.dropna()

# Print the first 5 rows
print(df.head())