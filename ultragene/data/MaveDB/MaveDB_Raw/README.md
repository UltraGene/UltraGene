# Software Engineering Documentation: JSON to CSV Data Processing Script

## Overview

This Python script is designed for processing JSON files and consolidating the extracted data into a CSV format. The script is particularly useful for handling large datasets, providing a structured approach to data transformation.

## Script Structure

### Imports and Dependencies

- **Pandas (pd)**: For data manipulation and analysis.
- **JSON**: To parse JSON formatted files.
- **Glob**: For file path pattern matching.
- **Pathlib (Path)**: For reliable file system path handling.
- **Argparse**: For parsing command-line options and arguments.

### Functions

#### `extract_mapped_scores(data, gene_name)`
- **Purpose**: Extracts and transforms 'mapped_scores' data from JSON into a DataFrame.
- **Parameters**:
  - `data`: JSON data containing 'mapped_scores'.
  - `gene_name`: Gene name extracted from the JSON data.
- **Returns**: A DataFrame with the processed data.

#### `process_json_files(directory_path)`
- **Purpose**: Processes all JSON files in a specified directory and merges them into a single CSV file.
- **Parameter**:
  - `directory_path`: Path to the directory with JSON files.
- **Process**:
  1. Reads each JSON file in the directory.
  2. Normalizes the JSON data into pandas DataFrame.
  3. Extracts relevant data using `extract_mapped_scores`.
  4. Appends the extracted data to a list of DataFrames.
  5. Concatenates all DataFrames into one and exports it as CSV.

### Main Function

#### `main()`
- **Functionality**: Sets up command-line argument parsing and initiates the JSON processing function.
- **Command-Line Argument**:
  - `directory_path`: Specifies the directory path containing JSON files.

### Execution Point

- **`if __name__ == "__main__":`**
  - Triggers the main function to execute the script.

## Usage

This script is executed via command line, where the user specifies the path to the directory containing the JSON files. The script efficiently processes the files, extracts the required data, and outputs a consolidated CSV file, making it an essential tool for data engineers working with JSON and CSV formats.
