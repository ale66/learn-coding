'''
Exercise file on operating with files.

This file has a proper main() and is callable: 

>python import_me.py

Moreover, this file can be imported:
Create a simple '.py' for yourself and put 'import import_me as load'
Now you can call load.loadtext(...)
'''

import csv

CUSTOMLENGHT = 120


def main():
	'''A simple example of text access, line by line
		followed by CSV line-by-line reading
	'''


	# change to reflect the situation on your own computer!

	# the double '\' is for Win systems, adapt as needed
	TXT = 'C:\\Users\\aless\\git\\learn-coding\\70-modules\\data\\hamlet.txt'

	CSV = 'C:\\Users\\aless\\git\\learn-coding\\70-modules\\data\\biostats.csv'

	loadtext(TXT, '\n')

	# uncomment as needed: why doesn't it work?
	# loadcsv(CSV, ',')

# consider the version with defaults
# def loadtext(my_file = TXT, my_delimit = '.'):
def loadtext(my_file, my_delimit):
	'''Takes a file name, opens is and prints it on the screen as list of sentences.
		define the second parameter to delimit each line to be printed
	'''

	with open(my_file) as f:

		read_text = csv.reader(f, delimiter = my_delimit)

		for _ in range(CUSTOMLENGHT):

			line = next(read_text)
			
			if line != '[]':
				print(line)
			
		for lines in read_text:
			print(lines)


def loadcsv(my_file, my_delimit):
	'''for reference'''
	
	with open(my_file) as f:
		read_csv = csv.reader(f, delimiter = my_delimit)

		for row in read_csv:
			print(row)

		line = next(read_csv)
		print(line)
		# why does it bomb?


# this call allows to call auxiliary 
# functions in main() before actually defining them 
if __name__ == '__main__':
	print('This is an exercise file with a couple of functions for reading files')
	main()
