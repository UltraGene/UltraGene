import pandas as pd
import json
import glob
import os

# Corrected the directory path to include a slash at the end
# directory_path = '<PATH>'

# Use os.path.dirname(os.path.abspath(__file__)) to get the current directory of the script
directory_path = os.path.dirname(os.path.abspath(__file__)) + '/'



# Using glob.glob to match the JSON file extension
json_files = glob.glob(directory_path + '*.json')

dataframes = []

for file_path in json_files:
    with open(file_path, 'r') as file:
        data = json.load(file)
        data = [data] if isinstance(data, dict) else data
        df = pd.json_normalize(data)

        gene_name = df['targetGene.name'].iloc[0] if 'targetGene.name' in df.columns else None

        # Check if 'mapped_scores' is in the DataFrame and it's not empty
        if 'mapped_scores' in df.columns and not df['mapped_scores'].isnull().all():
            # Extracting data from 'mapped_scores'
            for scores in df['mapped_scores'].dropna():
                extracted_data = [{
                    # 'gene_name': gene_name,
                    # 'start_value': item.get('post_mapped', {}).get('variation', {}).get('location', {}).get('interval', {}).get('start', {}).get('value'),
                    'end_value': item.get('post_mapped', {}).get('variation', {}).get('location', {}).get('interval', {}).get('end', {}).get('value'),
                    'Ref': item.get('post_mapped', {}).get('vrs_ref_allele_seq'),
                    'Alt': item.get('post_mapped', {}).get('variation', {}).get('state', {}).get('sequence'),
                    'Functional score': item.get('score')
                } for item in scores if item.get('post_mapped')]

                # Only append if extracted_data is not empty
                if extracted_data:
                    df_extracted = pd.DataFrame(extracted_data)
                    dataframes.append(df_extracted)

# Concatenate all the DataFrames into one if dataframes is not empty
if dataframes:
    final_df = pd.concat(dataframes, ignore_index=True)
    # Export the final DataFrame to a CSV file
    final_csv_path = directory_path + 'MaveDV_data.csv'
    final_df.to_csv(final_csv_path, index=False)
else:
    print("No dataframes were created, please check your JSON structure or 'mapped_scores' content.")
