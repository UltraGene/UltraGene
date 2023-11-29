import pandas as pd

def validate_and_load_snp_data(file_path):
    """
    Validate and load SNP data from a 23andMe file into a pandas DataFrame, 
    excluding rows with 'I' (Insertion), 'D' (Deletion), and '0' (no-call).

    'I' and 'D' represent genetic variations involving insertions or deletions 
    of nucleotides. '0' indicates a no-call, where the genotype at a specific 
    SNP could not be determined reliably, often due to low-quality data, 
    technical limitations, or absence of data.
    
    :param file_path: Path to the 23andMe data file.
    :return: Pandas DataFrame containing SNP data, excluding rows with 'I', 'D', or '0'.
    """
    expected_columns = ['rsid', 'chromosome', 'position', 'allele1', 'allele2']
    valid_bases = {'A', 'T', 'G', 'C', 'I', 'D', '0'}
    metadata_lines = 0

    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('#'):
                metadata_lines += 1
            else:
                columns = line.strip().split('\t')
                if columns != expected_columns:
                    raise ValueError("Unexpected file format. The file does not contain the expected columns.")
                break

    snp_df = pd.read_csv(file_path, sep='\t', skiprows=metadata_lines)

    if snp_df.isnull().values.any():
        raise ValueError("The file contains missing data.")

    # Count and exclude rows with 'I', 'D', or '0'
    excluded_counts = snp_df[(snp_df['allele1'].isin(['I', 'D', '0'])) | (snp_df['allele2'].isin(['I', 'D', '0']))].shape[0]
    snp_df = snp_df[~((snp_df['allele1'].isin(['I', 'D', '0'])) | (snp_df['allele2'].isin(['I', 'D', '0'])))]

    return snp_df, excluded_counts

if __name__ == "__main__":
    file_path = 'AncestryDNA_Raw_DNA_File.txt'
    try:
        snp_data, excluded_counts = validate_and_load_snp_data(file_path)
        print(f"Data loaded successfully. Rows excluded ('I', 'D', or '0'): {excluded_counts}")
        print(snp_data.head())
    except ValueError as e:
        print(e)