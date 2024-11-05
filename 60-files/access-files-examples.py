# make sure that Python runs in the local folder!

MYFILE = './data/incipit.txt'


'''
with open(MYFILE) as f:
    longstringwithnewlines = f.read()

print(longstringwithnewlines)
'''

'''
with open(MYFILE) as f:
  for line in f:
    print(line)
'''



# include foreign functions

import csv

FILE = './data/biostats.csv'


'''
with open(FILE) as f:

	lines = csv.reader(f, delimiter=',')

	for l in lines:
		print(l)
'''

'''
with open(FILE) as f:

    lines = csv.reader(f, delimiter=',')

    print('Interpretation schema:')

    # consume one line of lines
    header = next(lines)
    print(header)

    print('These are the values:')
    for l in lines:
        print(l)
'''


# import into dictionaries, use the schema on the first line

'''
with open(FILE) as f:

    lines = csv.DictReader(f,  delimiter=',')

    for l in lines:
        print(f'Patient: {l}')
'''


# data migration: use a Spanish-language schema

'''
first_line = ['Name', 'Sex', 'Age', 'Height(in)', 'Weight(lbs)']

mapping_es = ['Nombre', 'Sexo', 'Edad', 'Estatura(in)', 'Peso(lbs)']

with open(FILE) as f:

    lines = csv.DictReader(f,  fieldnames = mapping_es, delimiter = ',')

    for l in lines:
        print(f'Paciente: {l['Nombre'], l['Peso(lbs)'], l['Edad']}')
'''
