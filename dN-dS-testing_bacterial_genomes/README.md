## dN/dS selection analysis of core-genes

In this repository you find several scripts that form a small pipeline to process aligned core-genes. Clone the repository if you find it interesting and modify the scripts for your own use.

The pipeline calculate the pairwise dN/dS ratio's between all the genes in an alignment in order to determine if there is positive or purifying selection found between the genes of a species of interest. 

The genes need to have a `nucleotide similarity between 70 and 95 % `to give meaningful results. That will mostly be highly consevered genes.

The program Get_homologues can be use to determine the core-genes of a species using a nucleotide cut-off and outputs for each core-genes a fasta file with unaligned sequences

The unaligned sequences can be aligned using PRANK and the alignments need to by in the PHYLIP format `*.phy`

The pipeline needs several dependencies:

```
The evolutionary package: PAML
Biopython 
Biopython package: Bio.Phylo.PAML

```

The PAML package is used for the program `yn00`, which calculates the dN/dS ratio's and this program is called from the python script: `pw_flow.py.`. That script produces for every dN/dS method available and line with the results for each pairwise comparison. That line is written to a text-file, that collects all the pair-wise comparisons of all core-genes analyzed. In addition, will ot output a text file with the normal `yn00` output

The bash file:` Yn00Script_batch.sh` is placed in the folder (or your PATH) with all the aligned core-genes files. This script will can be run like any normal bash script.

The file: `yn00.ctl` is created for each gene by the script `pw_flow.py.` and is needed to run the `yn00` program.

The files in this repository.

```
Yn00Script_batch.sh
pw_flow.py
yn00.ctl

```

Thomas H.


