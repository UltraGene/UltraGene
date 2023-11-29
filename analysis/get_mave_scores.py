import pandas as pd
import json
import glob
from pathlib import Path
import argparse

def extract_mapped_scores(data, gene_name):
    """
    Extracts and transforms 'mapped_scores' data into a DataFrame.

    :param data: The JSON data containing 'mapped_scores'.
    :param gene_name: Extracted gene name from the JSON data.
    :return: A DataFrame with the extracted data.
    """
    extracted_data = [{
        'gene_name': gene_name,
        'start_value': item.get('post_mapped', {}).get('variation', {}).get('location', {}).get('interval', {}).get('start', {}).get('value'),
        'end_value': item.get('post_mapped', {}).get('variation', {}).get('location', {}).get('interval', {}).get('end', {}).get('value'),
        'Ref': item.get('post_mapped', {}).get('vrs_ref_allele_seq'),
        'Alt': item.get('post_mapped', {}).get('variation', {}).get('state', {}).get('sequence'),
        'Functional score': item.get('score')
    } for scores in data['mapped_scores'] for item in scores if 'post_mapped' in item]

    return pd.DataFrame(extracted_data) if extracted_data else pd.DataFrame()

def process_json_files(directory_path):
    """
    Processes all JSON files in a specified directory and consolidates them into a single CSV file.

    :param directory_path: Path to the directory containing JSON files.
    """
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
                    df_extracted = extract_mapped_scores(df, gene_name)
                    if not df_extracted.empty:
                        dataframes.append(df_extracted)
        except json.JSONDecodeError:
            print(f"Error decoding JSON in file {file_path}")
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")

    if dataframes:
        final_df = pd.concat(dataframes, ignore_index=True)
        final_csv_path = directory_path / 'mave_final_dataframe.csv'
        final_df.to_csv(final_csv_path, index=False)
        print(f"File successfully created at {final_csv_path}")

def main():
    parser = argparse.ArgumentParser(description='Process JSON files and consolidate into a single CSV file.')
    parser.add_argument('directory_path', type=str, help='Path to the directory containing JSON files')
    args = parser.parse_args()
    process_json_files(args.directory_path)

if __name__ == "__main__":
    main()
