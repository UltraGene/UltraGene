import streamlit as st
import pandas as pd
import subprocess
import os

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


def Matching():
    # Load the 'Sorted_MaveDB.csv' file
    df_sorted_mavedb = pd.read_csv('Sorted_MaveDB.csv')

    # Load the 'Sorted_Alpha_Test.csv' file
    df_sorted_alpha_test = pd.read_csv('Sorted_Alpha.csv')

    # Load the 'Cleaned_23andMe.csv' file
    df_cleaned_23andme = pd.read_csv('Cleaned_23andMe.csv')


    # Merging 'df_cleaned_23andme' with 'df_sorted_mavedb' on 'position' and 'Alt'
    df_23DB = pd.merge(df_cleaned_23andme, df_sorted_mavedb, on=['position', 'Alt'])

    # Removing duplicate rows from 'df_23DB'
    # df_23DB.drop_duplicates(inplace=True)

    # Dropping rows where 'Functional score' is greater than zero in 'df_23DB'
    df_23DB = df_23DB[df_23DB['Functional score'] <= 0]

    # Merging 'df_cleaned_23andme' with 'df_sorted_alpha_test' on 'position' and 'Alt'
    df_23Alpha = pd.merge(df_cleaned_23andme, df_sorted_alpha_test, on=['position', 'Alt'])

    # Removing duplicate rows from 'df_23Alpha'
    # df_23Alpha.drop_duplicates(inplace=True)

    # Dropping rows where 'Functional score' is greater or equal to zero in 'df_23Alpha'
    df_23Alpha = df_23Alpha[df_23Alpha['Functional score'] < 0]

    # Finding positions that appear in both 'df_23DB' and 'df_23Alpha'
    common_positions = df_23DB[df_23DB['position'].isin(df_23Alpha['position'])]

    # Saving the final data to a new CSV file
    common_positions.to_csv('common_positions.csv', index=False)

    # Saving the final data to a new CSV file
    df_23DB.to_csv('df_23DB.csv', index=False)


# Streamlit App implement
st.title("DNA Matching :dna:")

# File uploader widget
uploaded_file = st.file_uploader("Choose a file", type='txt')
if uploaded_file is not None:
    # Save the file
    with open("23andMe_data.txt", "wb") as f:
        f.write(uploaded_file.getbuffer())
    # st.success("File saved as 23andMe_data.txt")

    # Run the andME function and show success message
    andME()
    # st.success("Data sorted successfully in andME.")

    # Initialize a progress bar
    progress_bar = st.progress(0)

    # Run the Matching function with progress updates
    Matching()

    # Complete the progress bar
    progress_bar.progress(100, "Data matching successfully, please move to next step.")

    st.balloons()

