import pandas as pd

def validate_and_load__data(file_path):
    """
    Validate and load AncestryDNA data from a file into a pandas DataFrame,
    excluding rows where either allele is '0' (no-call).

    :param file_path: Path to the AncestryDNA data file.
    :return: Pandas DataFrame containing SNP data.
    :raises ValueError: If the file format is unexpected or contains invalid data.
    """
    try:
        # Reading the file with pandas, assuming tab-separated values and comments marked with '#'
        data = pd.read_csv(file_path, sep='\t', comment='#', header=0)

        # Validate if expected columns are present
        expected_columns = ['rsid', 'chromosome', 'position', 'allele1', 'allele2']
        if not all(column in data.columns for column in expected_columns):
            raise ValueError("File format is unexpected, missing required columns.")

        # Create a 'genotype' column by combining 'allele1' and 'allele2'
        data['genotype'] = data['allele1'] + data['allele2']

        # Exclude rows where either allele is '0'
        data_cleaned = data[(data['allele1'] != '0') & (data['allele2'] != '0')]

        return data_cleaned

    except Exception as e:
        # Handling exceptions related to file reading or format issues
        raise ValueError(f"Error reading file: {e}")

