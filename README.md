<h1 align="center" style="color: white; background-color: black; padding: 10px;">🧬 UltraGene</h1>

<p align="center">
    <b>Tool for Advanced DNA Mutational Signature Scanning for Precision Medicine</b>
    <br><br>
    <img src="img/dna1.gif" alt="DNA Animation" style="width: 60%; margin: auto; display: block;">
</p>


# UltraGene

List of Team Members and affiliations:
- CO | PhD Genetics @ University of Washington
- KC | MS Mechanical Engr. @ University of Washington
- Dana | MS Mechanical Engr. @ University of Washington
- Zi | MS Mechanical Engr. @ University of Washington

## Documentation

[UltraGene Documentation](https://github.com/UltraGene/ultragene.github.io)

## Project Goals

For more background and context see lecture [Understanding the Functional Effects of Genetic Variation At Scale](https://youtu.be/ChzOPm1-YfI?t=350)

UltraGene tackles a significant challenge in precision genomic medicine: the limited understanding of the functions of most human genetic variants. A large number of genetic variants found in clinical settings are categorized as Variants of Uncertain Significance (VUS), creating obstacles in clinical decision-making due to their unclear association with diseases. This problem is particularly severe for individuals from underrepresented research populations, thereby intensifying existing healthcare inequities.

The aim of this project is to enhance the clinical utility of precision genomic medicine.

Individuals will be able to upload their genetic data to be checked against:

1. **Functional Data from Multiplex Assays of Variant Effects (MAVEs)**: This involves acquiring data through Saturation Genome Editing to determine the functional impact of missense genetic variants.
2. **AlphaMissense In Silico Prediction**: Utilizing AlphaMissense, an in silico prediction tool, to assess the impact of missense variants on VUS, enhancing our understanding of their potential effects.
3. **Online Mendelian Inheritance in Man (OMIM) Analysis**: Integrating data from OMIM to understand inheritance patterns of genes, particularly focusing on whether mutations in a single allele or both alleles contribute to disease development.

This multifaceted approach is designed to provide a more comprehensive understanding of genetic variants, particularly VUS, thereby facilitating more informed clinical decisions and contributing to more equitable and effective genomic medicine practices.

# Streamlit Application Download Step

### Step1 Set up environment
``` shell
pip install streamlit
pip install pandas 
```

### Step2 Download Streamlit_app package

```shell
curl -o https://github.com/UltraGene/UltraGene/tree/main/Streamlit_App
```
### Run `database_setup.sh`to create the Streamlit databse files in current directory. 

### Step3
### Type "streamlit run Home.py" (The direction should be same as in Home.py)

### Step4
### Upload your 23andMe.tx file. (Makes sure your last column name should call genotype)
![My Animation](Matching.gif)

## After matching finished. You may download your each data .csv file.
![My Animation](Visual.gif)


## User Stories
User Stories [ UserStories ](https://github.com/UltraGene/UltraGene/blob/main/doc/UserStory.md)


## Approach
1. **Data Cleaning and Rearrangement:**
   - MaveDB and Alpha datasets are cleaned and rearranged for compatibility and efficiency.

2. **User Data Upload:**
   - Users upload their 23andMe genetic data into the system.

3. **Data Matching:**
   - The Streamlit app processes the uploaded 23andMe data.
   - It performs a matching operation with both MaveDB and Alpha datasets.

4. **Datasheet Generation:**
   - Two datasheets are generated post-matching:
     - `df_23DB`: Represents matches between user DNA and MaveDB.
     - `df_23Alpha`: Shows matches between user DNA and Alpha data.

5. **Visualization:**
   - Both datasheets (`df_23DB` and `df_23Alpha`) are displayed on the visualization pages within the app.

6. **Additional Analysis:**
   - A third datasheet, `common_position.csv`, is generated.
   - This datasheet contains positions where user DNA matches with both MaveDB and Alpha datasets.

7. **Risk Assessment:**
   - The app identifies and suggests the most dangerous DNA positions based on the common matches.


## Analysis of MaveDB, AlphaMissense

To process the raw data, we use:

* MaveDB script [ultragene/analysis/get_mave_scores.py](https://github.com/UltraGene/UltraGene/blob/main/analysis/get_mave_scores.py)

* AlphaMissense [AlphMissence Raw Data](https://console.cloud.google.com/storage/browser/dm_alphamissense;tab=objects?prefix=&forceOnObjectsSortingFiltering=false)

## Results

- **Overall Assessment:** Decent outcomes.
- **Performance:** Works effectively with input from 23andMe data.
- The integration process demonstrates satisfactory performance with 23andMe genetic data.
- The outcomes indicate a reliable level of accuracy and utility.

## Conclusions

The main goal is to provide users with a comprehensive understanding of their genetic data in relation to MaveDB and Alpha datasets, emphasizing potential health risks.

## Future Work
1. **Incorporation of Additional OpenSource Databases:**
   - Integrate more OpenSource databases to enrich the genetic data analysis capabilities.

2. **Support for Multiple Data Formats:**
   - Expand the data input compatibility to accept various formats.
   - Move beyond exclusive support for 23andMe data.
