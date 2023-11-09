import pandas as pd

# Load the CSV file, skipping initial spaces and ignoring lines that start with '#'
data = pd.read_csv('AlphaMissense_hg38.csv', skipinitialspace=True, comment='#')

# Step 2: Drop the columns 'Column2' and 'Column4'
# axis=1 denotes that we are referring to a column, not a row
#data = data.drop(['#CHROM', 'genome', 'uniprot_id', 'transcript_id', 'protein_variant', 'am_pathogenicity'], axis=1)
new_data = data.iloc[:, [1, 2, 3, -1]]

# Step 3: Save the modified DataFrame to a new CSV file
new_data.to_csv('Cleaned_AlphaMissense_hg38.csv', index=False)
