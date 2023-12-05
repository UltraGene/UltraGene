# Comprehensive Guide: Cleaning & Processing 23andMe Genetic Data

## Overview

This notebook offers a meticulous walkthrough of the procedures and functions employed to refine and process genetic data obtained from 23andMe. The approach ensures the integrity and relevance of the data for subsequent analysis.

## Process Breakdown

### 1. **Data Importation:**
   - **Function:** `pd.read_csv`
   - **Purpose:** To load the raw genetic data from '23andMe_data.txt' into a pandas DataFrame.
   - **Data Details:** The imported data encompasses columns like rsid, chromosome, position, and genotype.

### 2. **Primary Data Cleansing:**
   - **Approach:** Implementation of DataFrame methods.
   - **Objective:** To eliminate rows harboring empty values or '--' in the 'genotype' column, thereby retaining only legitimate genetic data.
   - **Significance:** Ensures data quality and reliability.

### 3. **Column Pruning:**
   - **Function:** `DataFrame.drop`
   - **Rationale:** To discard non-essential columns, specifically 'rsid' and 'chromosome'.
   - **Focus:** Streamlining the dataset by retaining columns pertinent to the analysis.

### 4. **Storing Refined Data:**
   - **Function:** `DataFrame.to_csv`
   - **Utility:** Facilitates the storage of processed data into CSV files at key stages.
   - **Advantage:** Provides convenient checkpoints for data retrieval and further analytical endeavors.

## Conclusion

This systematic approach to data cleaning and processing is integral in preparing the 23andMe genetic dataset for advanced analytical applications.
