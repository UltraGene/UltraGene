'''
This script is designed for processing JSON files containing genetic data and consolidating them into a single CSV file. 
It's structured to be used as a command-line tool. Here's an explanation of its components and functionality:

1. **Imports:**
   - `pandas` (as `pd`): Used for data manipulation and analysis.
   - `json`: To read JSON files.
   - `glob`: For file path pattern matching.
   - `pathlib.Path`: For handling filesystem paths in an object-oriented way.
   - `argparse`: For parsing command-line arguments.

2. **`process_json_files` Function:**
   - Purpose: Processes all JSON files in a specified directory.
   - `directory_path`: A `Path` object representing the directory containing JSON files.
   - `json_files`: Uses `glob` to find all files ending with `.json` in the specified directory.
   - `dataframes`: A list to accumulate data extracted from each JSON file.
   - Iterates over each JSON file:
     - Opens and reads the file.
     - If the file's root is a dictionary, it's converted into a list (to standardize the data structure).
     - `pd.json_normalize`: Flattens the JSON data into a pandas DataFrame.
     - Extracts `gene_name` from the 'targetGene.name' column, if available.
     - Checks for the 'mapped_scores' column. If present and not entirely null:
       - Iterates over each item in 'mapped_scores' (assumed to be a list of dictionaries).
       - Constructs a dictionary for each item with specific values extracted from nested structures.
       - These dictionaries are used to create a DataFrame (`df_extracted`) which is appended to `dataframes`.
   - Error Handling: Catches and prints exceptions that occur during file processing.
   - After all files are processed, concatenates all DataFrames in `dataframes` and writes the result to a CSV file.

3. **How to Use the Script:**
   - Run the script from the command line, providing the path to the directory containing the JSON files as an argument.
   - Example: `python get_mave_scores.py ../path/to/json_files/`

'''

import pandas as pd
import json
import glob
from pathlib import Path
import argparse

def process_json_files(directory_path):
    directory_path = Path(directory_path)
    json_files = directory_path.glob('*.json')
    dataframes = []

    for file_path in json_files:
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                data = [data] if isinstance(data, dict) else data
                df = pd.json_normalize(data)

                gene_name = df.get('targetGene.name').iloc[0] if 'targetGene.name' in df.columns else None

                if 'mapped_scores' in df.columns and not df['mapped_scores'].isnull().all():
                    for scores in df['mapped_scores'].dropna():
                        extracted_data = [{
                            'gene_name': gene_name,
                            'start_value': item.get('post_mapped', {}).get('variation', {}).get('location', {}).get('interval', {}).get('start', {}).get('value'),
                            'end_value': item.get('post_mapped', {}).get('variation', {}).get('location', {}).get('interval', {}).get('end', {}).get('value'),
                            'Ref': item.get('post_mapped', {}).get('vrs_ref_allele_seq'),
                            'Alt': item.get('post_mapped', {}).get('variation', {}).get('state', {}).get('sequence'),
                            'Functional score': item.get('score')
                        } for item in scores if item.get('post_mapped')]

                        if extracted_data:
                            df_extracted = pd.DataFrame(extracted_data)
                            dataframes.append(df_extracted)
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")

    if dataframes:
        final_df = pd.concat(dataframes, ignore_index=True)
        final_csv_path = directory_path / 'mave_final_dataframe.csv'
        final_df.to_csv(final_csv_path, index=False)
        print(f"File successfully created at {final_csv_path}")

def main():
    parser = argparse.ArgumentParser(description='Process some json files.')
    parser.add_argument('directory_path', type=str, help='The directory containing the json files')
    args = parser.parse_args()
    process_json_files(args.directory_path)

if __name__ == "__main__":
    main()