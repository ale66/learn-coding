'''
test local modules: include a set of functions from a separate Python file.
In this case the module to be imported sits in the same folder
'''

import import_me as me


# me.loadtext('..\data\hamlet.txt', '\n')

# for VS Code excution edit the absolute path to the source text
HAMLET = "C:\\Users\\ale\\Downloads\\git\\learn-coding\\70-modules\\data\\hamlet.txt"

me.loadtext(HAMLET, '.')

# uncomment to run
# DATA = '../data/biostats.csv'
# me.loadcsv(DATA, ',')