'''
Exercise file on operating with files.

This file has a proper main() and is callable
'''

import csv
#import pandas

INCIPITLENGHT = 120

# change to reflect the situation on your own computer!

# the double '\' is for Win systems, adapt as needed
TXT = "C:\\Users\\ale\\git\\learn-coding\\70-modules\\data\\hamlet.txt"

CSV = "C:\\Users\\ale\\git\\learn-coding\\70-modules\\data\\biostats.csv"

def main():
	'''Simple text access, line by line
		followed by CSV line-by-line reading
	'''

	loadtext(TXT)

	# uncomment as needed
	#loadcsv(CSV, ',')


def loadtext(myfile):
	with open(myfile) as f:

		readtext = csv.reader(f, delimiter='.')

		for _ in range(INCIPITLENGHT):
			line = next(readtext)
			if line != '[]':
				print(line)
			
		#for lines in readtext:
		#	print(lines)

def loadcsv(my_file, my_delimit):
	'''for reference'''
	
	with open(my_file) as f:
		readCSV = csv.reader(f, delimiter = my_delimit)

		for row in readCSV:
			print(row)

		# First line is the header		
		line = next(readCSV)
		print(line)
		# doesn't work as it is, why?

# this call allows to call auxiliary 
# functions before actually defining them 
main()
