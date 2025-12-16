# maybe-usefull-stuff
A repository with scripts that could be usefull for others.

Use at your own risk.

## how to install checkm using a virtual environment
[See these instructions](Install_checkM_in_a_virtual_environment.md)

## a script to parse the data from microbecensus
[python2: AVG_output_parser.py ](AVG_output_parser.py)

## Calculation dN/dS ratios from bacterial genomes
[dN-dS testing bacterial genomes](dN-dS-testing_bacterial_genomes/README.md)

## a phylogseq tutorial
viewing the html page:[Phyloseq tutorial html page](phyloseq_tutorial.html)

viewing the github formated document:[Phyloseq github](phyloseq_tutorial.md)

## Comparing bacterial genomes with MASH and FastANI
[Comparison of Vibrionales genome similarity](genome_comparison/Comparison_of_Vibrionales_genome_similarity.md)

## Extract multipage tables from long PDF files
[python2: pdf_extract_to_tsv.py](https://github.com/Thomieh73/Useful_scripts/blob/master/pdf_extract_to_tsv.py)

Since Excel only can handle one page at the time, I created this script to pull tables from multiple pages in one go. The script was created using google gemini.

This script takes a PDF file, and it needs to know the pages where the table is found. It will produce a table and output it as a tabular file. 
Note that the table extraction is not perfect, but that is mostly due to the way the original table was created. 
Thus check the output carefully, and correct some of the errors using vscode.

Before using this script make sure you have python 2 installed, and the dependencies, camelot, pandas.
Dependencies can be installed with the pip command:
```
 pip install camelot-py[cv] pandas
```
To run the script in the folder of your choice and parsing the table found on pages 12 to 23 do:
```
python pdf_extract_to_tsv.py YOUR_FILE.pdf 12-23
```
The out put is a file called: YOUR_FILE.tsv. That can be imported in excel, or a text editor.
