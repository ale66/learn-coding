# Statistical analysis of Shakespeare's text:
# Question: which character did he use most frequently?

# A large stats from the British Library corpora suggests that 
# 'E/e' is the most frequent English language letter.
# Challenges:
# 
# is this the case for Shakespeare's writings? 
# 
# is this also true for Italian?

# From the Gutenberg project
EN = '''Two households, both alike in dignity,
In fair Verona, where we lay our scene,
From ancient grudge break to new mutiny,
Where civil blood makes civil hands unclean.
From forth the fatal loins of these two foes
A pair of star-cross'd lovers take their life;
Whose misadventur'd piteous overthrows
Doth with their death bury their parents' strife.
The fearful passage of their death-mark'd love,
And the continuance of their parents' rage,
Which, but their children's end, nought could remove,
Is now the two hours' traffic of our stage;
The which, if you with patient ears attend,
What here shall miss, our toil shall strive to mend.'''


# from the Le Mornier Italian edition, 1869
IT = '''Due famiglie, spettabili entrambe per grado, vengono alle prese nella gentil Verona, 
ove è posta la nostra scena, e di sangue civile si arrossano le contrade. 
Due stipiti ostili discendono due amanti infelici, che colla loro morte pongono fine ai litigi antichi 
delle loro case. 
Nel lasso di due ore vedrete le terribili vicissitudini dell'amore, e un infuriare 
che non si tronca che per una sventura orrenda, e se vorrete udirci con pazienza, 
cercheremo di riparare, colle nostre fatiche agli errori che per avventura potessero riscontrarsi 
in questo racconto.'''

# You're welcome to contribute another language you like (Latin characters please)

# shakespeare_signature = {'Juliet':85, 'Romeo':60, 'Verona':20,   }

# what we'll get:
# stats_en = {'V':1, 'e':1, 'r':1, 'o':1, 'n':1, 'a':1, ' ':100, '!':17 ...}

# toggle this to run on different languages
mytext = EN

# --- Coding exercise: 
# extract a text morphology 
# by counting relative character frequencies


# some baseline code, edit it to solve the challenge

text_length = len(mytext)

# prepare a dictionary to store the counting as we go down the text
mystats = {}


# Count occurrences 
for c in mytext:

    if c in mystats:
        # this char. has been seen already
        mystats[c] += 1

    else:
        mystats[c] = 1

print('Morphology by char. frequency in English:')

# Computing relative frequencies

if text_length > 0:

    # mind the variable names
    for key, val in mystats.items():

        mystats[key] = val/text_length
        
        print(f'{key} --> {val}')

# -------------- Complete at home:

# rebase the frequencies to make them more readable:

# e.g., from 'e --> 0.09335443037974683' to 'e: 9.33%'


# ------------------- This part is for reference only ---------------------

# Present the characters in decreasing frequency order

# Uncomment and run to see how lambdas work

# As dictionaries are inherently unsorted data structures, 
# a list of tuples is created instead


'''
sorted_stats_en = sorted(mystats.items(), key = lambda its_key: its_key[1], reverse=True)

# notice the reverse logic of the lambda:
# given a value, position '1', find it relative key, 'its_key'

for key, val in sorted_stats_en:
    print(f'{key} --> {val}')

print(sorted_stats_en)
'''

# --- For Reference: Data visualisation

import numpy as np
import matplotlib.pyplot as plt

keys = sorted(mystats)

# how many pairs are in the dictionary?
l = len(keys)

# enumerate the 'x' positions on the diagram: 0, 1, ... l-1
pos = np.arange(l)

# fix the width of each bar
bar_width = 0.5

plt.figure(figsize=(14, 5))
plt.bar(pos, [mystats[k] for k in keys], bar_width, label="EN")

# Compare with another language!
# copy+paste the code above to run for a second language, obtain, e.g., mystats_it
# change B -> your language code
# plt.bar(pos, [mystats_it[k] for k in keys], bar_width, label="IT")
# make it look better by pos -> pos+0.2 or something like that


plt.xticks(pos, keys)
plt.ylabel("frequency")
plt.legend()
plt.tight_layout()
plt.show()
