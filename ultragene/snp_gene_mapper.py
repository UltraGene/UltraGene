import requests

API_BASE_URL = "https://clinicaltables.nlm.nih.gov/api/snps/v3/search"

def fetch_gene_name(snp_id):
    """
    Fetch the gene name associated with the given SNP ID from 23andME raw text file.

    :param snp_id: The SNP ID (e.g., rs116587930).
    :return: The gene name associated with the SNP ID or an error message.
    """
    try:
        # Constructing the API URL with required parameters
        params = {
            "terms": snp_id,
            "ef": "38.gene",  # Fetching gene name for GRCh38 assembly
            "cf": "rsNum"     # Reference SNP accession number
        }
        response = requests.get(API_BASE_URL, params=params)

        # Check if the response is successful
        if response.status_code != 200:
            return "Error: Unable to fetch data from the API."

        data = response.json()
        
        # Extracting gene name
        gene_names = data[3][0][-1] if data[3] else "No gene name found for the given SNP ID."

        return gene_names
    except Exception as e:
        return f"An error occurred: {e}"

# # Example usage
# snp_id = "rs116587930"  # Example SNP ID
# gene_name = fetch_gene_name(snp_id)
# print(f"Gene name for SNP ID {snp_id}: {gene_name}")
