#!/bin/bash

# This script is designed to concatenate and unzip files that are split into smaller parts.
# The need for this script arises because the original files are too large to be uploaded
# to GitHub in one piece. As a workaround, files are split and uploaded in parts (e.g., Alphaa*)
# and then reassembled using this script. This is particularly useful for reassembling large
# datasets or files that have been segmented due to size constraints.


# Concatenate MaveDB files into a zip file
cat MaveDBa* > Sorted_MaveDB.csv.zip

# Concatenate Alpha files into a zip file
cat Alpha* > Sorted_Alpha.csv.zip

# Unzip the concatenated files
unzip Sorted_MaveDB.csv.zip
unzip Sorted_Alpha.csv.zip
