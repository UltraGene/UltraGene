import pandas as pd

# Load the dataframe
df = pd.read_csv('MaveDB.csv')

# Sort the dataframe by the first column
df_sorted = df.sort_values(by=df.columns[0])

# Drop rows with any NaN values
df_sorted = df_sorted.dropna()

# Save the sorted dataframe to a new csv file
df_sorted.to_csv('sorted_MaveDB.csv', index=False)
print(df_sorted.head())