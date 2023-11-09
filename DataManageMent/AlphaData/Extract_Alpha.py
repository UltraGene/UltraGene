import pandas as pd
import csv

# Open the TSV file and read its contents
with open('AlphaMissense_hg38.tsv', 'r') as tsv_file:
    tsv_reader = csv.reader(tsv_file, delimiter='\t')

    # Open a new CSV file for writing the converted content
    with open('AlphaMissense_hg38.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Read each line from TSV and write to CSV
        for line in tsv_reader:
            csv_writer.writerow(line)

