'''
test local modules: include a set of functions from a separate Python file.
In this case the module to be imported sits in the same folder
'''

import import_me as me


# me.loadtext('..\data\hamlet.txt', '\n')

# for VS Code excution edit the absolute path to the source text
HOME_DIR = "C:\\Users\\aless\\Downloads\\_git\\learn-coding\\70-modules\\"
 
TEXT_EXAMPLE = "data\\hamlet.txt"

me.loadtext(HOME_DIR+TEXT_EXAMPLE, '.')

# uncomment to fix & run
# DATA_EXAMPLE = '../data/biostats.csv'
# me.loadcsv(DATA_EXAMPLE, ',')