import pandas as pd
import json
import glob

# Change your path
directory_path = 'C:/Users/ROG/PycharmProjects/data/Gene/'

json_files = glob.glob(directory_path + '*.json')

dataframes = []

for file_path in json_files:
    with open(file_path, 'r') as file:
        data = json.load(file)
        if isinstance(data, dict):
            data = [data]
        df = pd.json_normalize(data)

        # Initialize lists to store extracted values
        start_values = []
        end_values = []
        Ref = []
        Alt = []
        Functional_Score = []

        # Check if 'mapped_scores' is in the DataFrame and it's not empty
        if 'mapped_scores' in df.columns and not df['mapped_scores'].isnull().all():
            # Loop through each item in 'mapped_scores'
            for item in df['mapped_scores'].iloc[0]:
                # Use the get method to avoid KeyError if the key does not exist
                post_mapped = item.get('post_mapped')
                if post_mapped:
                    variation = post_mapped.get('variation')
                    if variation:
                        location = variation.get('location')
                        if location:
                            interval = location.get('interval')
                            if interval:
                                start = interval.get('start')
                                end = interval.get('end')
                                if start and end:
                                    # start_values.append(start.get('value'))
                                    end_values.append(end.get('value'))
                                Ref.append(post_mapped.get('vrs_ref_allele_seq'))
                                Alt.append(variation.get('state', {}).get('sequence'))
                                Functional_Score.append(item.get('score'))

        # Create a DataFrame from the extracted values
        df_extracted = pd.DataFrame({
            # 'start_value': start_values,
            'Position': end_values,
            'Ref': Ref,
            'Alt': Alt,
            'Functional score': Functional_Score
        })

        # Append the DataFrame to the list
        dataframes.append(df_extracted)


# Concatenate all the DataFrames into one
final_df = pd.concat(dataframes, ignore_index=True)

# Optional: Extract specific items if needed
# final_df = final_df[['item1', 'item2', 'item3']]

# Export the final DataFrame to a CSV file
#final_csv_path = '/mnt/data/Gene/final_dataframe.csv'
final_df.to_csv(directory_path + 'final_dataframe.csv', index=False)