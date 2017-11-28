#! /usr/bin/python

# This script can be used to calculate pairwise statistics on codon-aware aligned nucleotide sequences
# it needs the biopython implementation of PAML and uses the YN00 program
# It takes a PHYLIP formatted alignment file and a name for an output file. 
# The later is needed for input into the required ctl file for YN00: "yn00.ctl"
# The output of each method to calculate dn/ds is APPENDED for each pairwise comparison to a specific output file
#

# USAGE AT YOUR OWN RISK:
# The command is like this: python pw_selection.py phylip_file.phy out_filename
# 
# Created by T.H.A. Haverkamp 20171115

#loading libraries
import os
import sys

#Loading the file:
from sys import argv

# load the yn00 module from Bio.Phylo.PAML
from Bio.Phylo.PAML import yn00

#This program takes two inputs: the alignment in phylip format, and outputfile name
#It returns a nested dictionary with various results depending on analysis
if len(sys.argv) != 3:
        print "Error.  There should be two inputs. An alignment in pyhlip format and the name for the output file"
#quit()

# small test
if len(sys.argv) >= 2:
        print "Super. We are processing", sys.argv[1]
#quit()


# Runn yn00

yn = yn00.Yn00()

yn.alignment = sys.argv[1]
yn.out_file = sys.argv[2]
yn.write_ctl_file()

yn.read_ctl_file("yn00.ctl") ##CTL File. See PAML manual for format.

name=yn.alignment
print "input-file: ", name
name2=yn.out_file
print name2
name3=name[0:5]+"_omega.out"
print name3
#with open (yn.out_file, 'w') as results: # output file

results = yn.run(ctl_file="yn00.ctl", verbose=False, command="yn00", parse=True)

#parsing the output file into a tabular file fot the YN00 method
print "parsing YN00 output for the Yang & Nielsen (2000) method"
with open("TAFF_selection_YN00.txt", 'a') as outfile: # output file
	for k, v in results.items():
		for k1, v1 in v.items():
			#print
			#print k, k1
			method1 = v1.get("YN00")
			#print method1
			New_line= []
			New_line.extend(method1.values())
			outfile.writelines(sys.argv[1] + "\t" + k + "\t" + k1 + "\t" + "\t".join([str(i) for i in New_line]) + "\n")   # writing original filename, parsed data, linebreak.

#parsing the output file into a tabular file fot the NG86 method
print "parsing YN00 output for the Nei-Gojobori (1986) method"
with open("TAFF_selection_NG86.txt", 'a') as outfile: # output file
	for k, v in results.items():
		for k1, v1 in v.items():
			method1 = v1.get("NG86")
			New_line= []
			New_line.extend(method1.values())
			outfile.writelines(sys.argv[1] + "\t" + k + "\t" + k1 + "\t" + "\t".join([str(i) for i in New_line]) + "\n")   # writing original filename, parsed data, linebreak.

#parsing the output file into a tabular file fot the LWL85 method
print "parsing YN00 output for the LWL85 method"
with open("TAFF_selection_LWL85.txt", 'a') as outfile: # output file
	for k, v in results.items():
		for k1, v1 in v.items():
			method1 = v1.get("LWL85")
			New_line= []
			New_line.extend(method1.values())
			outfile.writelines(sys.argv[1] + "\t" + k + "\t" + k1 + "\t" + "\t".join([str(i) for i in New_line]) + "\n")   # writing original filename, parsed data, linebreak.


#parsing the output file into a tabular file fot the LWL85m method
print "parsing YN00 output for the LWL85m method"
with open("TAFF_selection_LWL85m.txt", 'a') as outfile: # output file
	for k, v in results.items():
		for k1, v1 in v.items():
			method1 = v1.get("LWL85m")
			New_line= []
			New_line.extend(method1.values())
			outfile.writelines(sys.argv[1] + "\t" + k + "\t" + k1 + "\t" + "\t".join([str(i) for i in New_line]) + "\n")   # writing original filename, parsed data, linebreak.

#parsing the output file into a tabular file fot the LPB93 method
print "parsing YN00 output for the LPB93 method"
with open("TAFF_selection_LPB93.txt", 'a') as outfile: # output file
	for k, v in results.items():
		for k1, v1 in v.items():
			method1 = v1.get("LPB93")
			New_line= []
			New_line.extend(method1.values())
			outfile.writelines(sys.argv[1] + "\t" + k + "\t" + k1 + "\t" + "\t".join([str(i) for i in New_line]) + "\n")   # writing original filename, parsed data, linebreak.

print
print "finished analysis and parsing of: ", sys.argv[1]

exit()