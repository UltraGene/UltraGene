import pandas as pd

def andME():
    # Load the data
    file_path = '23andMe_data.txt'
    data = pd.read_csv(file_path, sep='\t', comment='#', header=None)

    # Renaming columns for clarity
    # Assuming the columns represent ['rsid', 'chromosome', 'position', 'genotype']
    data.columns = ['rsid', 'chromosome', 'position', 'genotype']

    # Sorting the data
    # Assuming sorting by 'chromosome' and 'position' in ascending order
    sorted_data = data.sort_values(by=['chromosome', 'position'])

    # Dropping rows with empty values or '--' in the 'genotype' column
    filtered_data = sorted_data[sorted_data['genotype'] != '--']

    # Dropping the 'rsid' and 'chromosome' columns
    final_data = filtered_data.drop(['rsid', 'chromosome'], axis=1)

    # Correcting the code to split the genotype column into separate rows
    # First, we need to revert to the data before dropping 'rsid' and 'chromosome' columns
    final_data = filtered_data.drop(['rsid', 'chromosome'], axis=1)

    # Now, splitting the genotype column
    expanded_data = final_data.set_index('position')['genotype'].apply(list).explode().reset_index()

    # Renaming the column for clarity
    expanded_data.columns = ['position', 'genotype']

    # Renaming the 'genotype' column to 'Ref' and creating the 'Alt' column
    expanded_data.rename(columns={'genotype': 'Alt'}, inplace=True)

    # Sort the dataframe by the first column
    expanded_data = expanded_data.sort_values(by=expanded_data.columns[0])

    # Saving the updated data to a new CSV file
    expanded_data.to_csv('Cleaned_23andMe.csv', index=False)