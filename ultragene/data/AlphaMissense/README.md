# Detailed Markdown Description of Code Steps

## Detailed Step-by-Step Code Description

1. **Reading the CSV File**: Used `pd.read_csv()` to load the 'Alpha.csv' file into a pandas DataFrame.

2. **Renaming Columns**: Utilized `DataFrame.columns` attribute to rename columns to specific names like 'CHROM', 'position', 'Ref', 'Alt' , etc.

3. **Column Selection**: Used DataFrame indexing to retain only the columns 'position', 'Ref', 'Alt', and 'Functional score', discarding others.

4. **Saving to CSV**: Employed `DataFrame.to_csv()` to save the final DataFrame as 'Sorted_Alpha.csv', without the index.

