import pandas as pd

# Load the CSV file
alpha_df = pd.read_csv('AlphaMissense_hg38.csv', skiprows=[0, 1, 2])

# Display the first few rows of the dataframe
print(alpha_df.head())

# Renaming each column
alpha_df.columns = ['CHROM', 'position', 'Ref', 'Alt', 'genome', 'uniprot_id', 'transcript_id', 'protein_variant', 'am_pathogenicity', 'Functional score']

# Display the modified DataFrame
print(alpha_df.head())

# Keeping only the specified columns
alpha_df = alpha_df[['position', 'Ref', 'Alt', 'Functional score']]

class_mapping = {'likely_pathogenic': -1, 'likely_benign': 1, 'ambiguous': 0}
alpha_df['Functional score'] = alpha_df['Functional score'].map(class_mapping)

# Sort the dataframe by the first column
alpha_df = alpha_df.sort_values(by=alpha_df.columns[0])

# Display the modified DataFrame
print(alpha_df.head())

# Saving the DataFrame to a CSV file
alpha_df.to_csv('Sorted_Alpha.csv', index=False)
