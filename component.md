Name:ValidateInput
what it does:
-Customers need to pass their raw gene sequence data files.
-Check the format, and it need to be like 23andme.
-IF\f it matches, then accept the data for further process; if not, give an error and reject.
Inpus:
-Gene sequence data files(text.file, and  show first three rows)
rsid	chromosome	position	genotype
rs62053747	17	1389    	AG
rs17606525	17	3104    	CC
rs6565703	17	12344   	AC
OUtpus:
-Boolean(If matches, then True, If not, then False)
