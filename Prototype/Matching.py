import pandas as pd

# Load the 'Sorted_MaveDB.csv' file
df_sorted_mavedb = pd.read_csv('Sorted_MaveDB.csv')

# Load the 'Sorted_Alpha_Test.csv' file
df_sorted_alpha_test = pd.read_csv('Sorted_Alpha.csv')

# Load the 'Cleaned_23andMe.csv' file
df_cleaned_23andme = pd.read_csv('Cleaned_23andMe.csv')

"""-----------------------------------------------------------"""

# Merging 'df_cleaned_23andme' with 'df_sorted_mavedb' on 'position' and 'Alt'
df_23DB = pd.merge(df_cleaned_23andme, df_sorted_mavedb, on=['position', 'Alt'])

# Removing duplicate rows from 'df_23DB'
df_23DB.drop_duplicates(inplace=True)

# Dropping rows where 'Functional score' is greater than zero in 'df_23DB'
df_23DB = df_23DB[df_23DB['Functional score'] <= 0]

print(df_23DB)
print(df_23DB.count())


"""-----------------------------------------------------------"""


# Merging 'df_cleaned_23andme' with 'df_sorted_alpha_test' on 'position' and 'Alt'
df_23Alpha = pd.merge(df_cleaned_23andme, df_sorted_alpha_test, on=['position', 'Alt'])

# Removing duplicate rows from 'df_23Alpha'
df_23Alpha.drop_duplicates(inplace=True)

# Dropping rows where 'Functional score' is greater or equal to zero in 'df_23Alpha'
df_23Alpha = df_23Alpha[df_23Alpha['Functional score'] < 0]

print(df_23Alpha)
print(df_23Alpha.count())


"""-----------------------------------------------------------"""

# Finding positions that appear in both 'df_23DB' and 'df_23Alpha'
common_positions = df_23DB[df_23DB['position'].isin(df_23Alpha['position'])]
print(common_positions)
