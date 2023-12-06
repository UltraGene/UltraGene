import requests
import logging

# Constants
API_BASE_URL = "https://clinicaltables.nlm.nih.gov/api/snps/v3/search"

def is_valid_snp_id(snp_id):
    """
    Validate the SNP ID format.

    :param snp_id: The SNP ID to validate.
    :return: Boolean indicating whether the SNP ID is valid.
    """
    return snp_id.startswith('rs') and snp_id[2:].isdigit()

def make_api_request(snp_id, assembly='38'):
    """
    Make an API request to fetch SNP data.

    :param snp_id: The SNP ID.
    :param assembly: The genome assembly version (e.g., '37' or '38').
    :return: The response JSON or None if an error occurs.
    """
    try:
        params = {
            "terms": snp_id,
            "ef": f"{assembly}.gene",
            "cf": "rsNum"
        }
        response = requests.get(API_BASE_URL, params=params)

        if response.status_code != 200:
            logging.error(f"API call failed with status code: {response.status_code}")
            return None

        return response.json()
    except requests.RequestException as req_err:
        logging.error(f"Request error: {req_err}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

    return None

def fetch_gene_name(snp_id, assembly='38'):
    """
    Fetch the gene name associated with the given SNP ID.

    :param snp_id: The SNP ID (e.g., rs116587930).
    :param assembly: The genome assembly version (e.g., '37' or '38').
    :return: The gene name associated with the SNP ID or an error message.
    """
    if not is_valid_snp_id(snp_id):
        return "Invalid SNP ID format."

    data = make_api_request(snp_id, assembly)

    if data is None:
        return "Error: Unable to fetch data from the API."

    # Extracting gene name
    gene_name = data[3][0][-1] if data[3] else "No gene name found for the given SNP ID."
    return gene_name


# snp_id = "rs122232"  # Example SNP ID
# gene_name = fetch_gene_name(snp_id)
# print(gene_name)
