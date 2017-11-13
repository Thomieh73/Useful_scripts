#! /usr/bin/python

# This script can be used to read the microbecensus tool output for several metagenomic samples.
# https://github.com/snayfach/MicrobeCensus
# It takes the input file it then appends a single line of tabulated text to given output file.
# the command is like this: python AVG_out_parser.py filename out_filename
# created by T.H.A. Haverkamp – 20171113

#loading libraries
import os
import sys

#Loading the file:
from sys import argv

# open the text file
with open(sys.argv[2], 'a') as outfile:  # appending to text file "a" 
	with open (sys.argv[1]) as infile:
		lines_after_10 = infile.readlines()[10:] # this skips the first 10 lines of the microbecensus output.
		New_line= []  # creating a NEW list
		for line in lines_after_10:
			New_line.extend(line.split())  # Adding each line in lines_after_10, to the samle line in New_line
	
		print New_line
				
		outfile.writelines(sys.argv[1] + "\t" + "\t".join(New_line) + "\n")   # writing original filename, parsed data, linebreak.

