Name:ValidateInput

What it does:
-Customers need to pass their raw gene sequence data files.(eg. 23andMe format txt file)
-Check the format, and it need to be like 23andMe.
-If it matches, then accept the data, and converting text file to pandas dataframe; If not, print("Wrong data format. Please upload 23andMe format.")

Inpus:
-Gene sequence data files(text.file, and  show first three rows)
rsid		chromosome	position	genotype
rs62053747	17		1389    	AG
rs17606525	17		3104    	CC
rs6565703	17		12344   	AC

Outputs:
-Boolean(If matches with the format, then True, converting text file to pandas dataframe(Database_23); If not, then False, print("Wrong data format. Please upload 23andMe format!"))


Name:Database_23

What it does:
-Contains the raw gene sequence after customers uploaded.
-Match its "chromosome", "position", "genotype" with Database_MaveDB and Database_AlphaMissence individually.

Inputs:
-ValidateInput

Outputs:
-Extracted data "chromosome", "position", "genotype" from Database_23

How it interact with other components:
-Saving the data that be converted from ValidateInput.
-Extract "chromosome", "position", "genotype", then match this data with Database_MaveDB and Database_AlphaMissence.


Name:Database_MaveDB

What it dose:
-It is a databse that contain each gene sequence and functional score in it.
-Originaly they were JSON file, convert into pandas formt, also clean the data.
-Extract Ref. and Alt. and Position. and Functional score in to as a new pandas data frame(Name: Database_MaveDB).
-Match with Database_23 and then save as a Database_Mutation.

Inputs:
-Database_23 extrated data "chromosome", "position", "genotype"

Outputs:
-Database_Mutation

How it interact with others component:
- Match with Database_23, and then save the result as Database_Mutation.


Name: Database_Mutation

What it does:
-Saving the matching result from Database_23 and Database_MaveDB.
-Add a new column named "Good/Bad gene", it save the calculation result: If "Functional score" is greater than 0, it will save benign gene; if "Functional score" is smaller than 0, it will save malignant gene.
-Extract "position", then matches with Database_AlphaMissence.

Inputs:
-The matching result from Database_23 and Database_MaveDB

Outputs:
-Database_Mutation with a new column of "Good/Bad gene"

How it interact with other components:
-Save the matching result from Database_23 and Database_MaveDB.
-Matches with Database_AlphaMissence by using "position" in Database_Mutation.


Name: Database_AlphaMissence

What it does:
-Matches with Databse_Mutation, extract Gene name from Database_AlphaMissence and output the defect Gene name.

Inputs:
-Database_Mutation

Outputs:
-Database_mutation with a new column of "Gene Name"

How it interact with other components:
-Match with  Database_Mutation and save it into a new Database_Mutation adda a new column it called "Gene Name".
 

Name: PopUpResult

What it does:
-Manifest the result(Gene name, Functional Score, Good/Bad gene) from Database_Mutation.

Inputs:
-Database_Mutation

Outputs:
-Gene name, Functional Score, Good/Bad gene

How it interact with other components:
-Get the result from Database_Mutation
-Extract "Gene name", "Functional score", "Good/Bad gene"
