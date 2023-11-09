import pandas as pd

# Load the CSV file
alpha_df = pd.read_csv('AlphaMissense_hg38.csv', skiprows=[0, 1, 2])

# Display the first few rows of the dataframe
print(alpha_df.head())

# Renaming each column
alpha_df.columns = ['CHROM', 'POS', 'REF', 'ALT', 'genome', 'uniprot_id', 'transcript_id', 'protein_variant', 'am_pathogenicity', 'am_class']

# Display the modified DataFrame
print(alpha_df.head())

# Keeping only the specified columns
alpha_df = alpha_df[['POS', 'REF', 'ALT', 'am_class']]

# Display the modified DataFrame
print(alpha_df.head())

# Saving the DataFrame to a CSV file
alpha_df.to_csv('Sorted_Alpha.csv', index=False)
