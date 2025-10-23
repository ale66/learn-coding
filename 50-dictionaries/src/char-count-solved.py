# stats_enistical analysis of Shakespare's text:
# Question: which character did he use most frequently?

# A large stats from the British Library corpora suggests that 
# 'E/e' is the most frequent English language letter.
# Challenges:
# 
# is this the case for Shakespare's writings? 
# 
# is this also true for Italian?

# From the Gutemberg project
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


# from the Le Mornier edition, 1869
IT = '''Due famiglie, spettabili entrambe per grado, vengono alle prese nella gentil Verona, 
ove è posta la nostra scena, e di sangue civile si arrossano le contrade. 
Due stipiti ostili discendono due amanti infelici, che colla loro morte pongono fine ai litigi antichi 
delle loro case. 
Nel lasso di due ore vedrete le terribili vicissitudini dell'amore, e un infuriare 
che non si tronca che per una sventura orrenda, e se vorrete udirci con pazienza, 
cercheremo di riparare, colle nostre fatiche agli errori che per avventura potessero riscontrarsi 
in questo racconto.'''

# You're welcome to contribute another language you like (Latin characters please)

# shakespare_signature = {'Juliet':85, 'Romeo':60, 'Verona':20,   }

# what we'll get:
# stats_en = {'V':1, 'e':1, 'r':1, 'o':1, 'n':1, 'a':1, ' ':100, '!':17 ...}

mytext = EN

mystats = {}

for c in mytext:
    if c in mystats:
        # this char. has been seen already
        mystats[c] += 1
    else:
        mystats[c] = 1

print('Morphology by char. frequency in English:')
# print(stats_en)

# Computing relative frequencies

text_lenght = len(mytext)

if text_lenght >0:
    # mind the variable names
    for key, val in mystats.items():

        mystats[key] = val/text_lenght
        
        print(f'{key} --> {val}')


#------------------- This part is for reference only ---------------------

# Now, present the characters in decreasing frequency order

# As dictionaries are inherently unsorted data structures, 
# a list of tuples is created instead
sorted_stats_en = sorted(mystats.items(), key = lambda its_key: its_key[1], reverse=True)
# notice the reverse logic of the lambda:
# given a value, position '1', find it relative key, 'its_key'
for key, val in sorted_stats_en:
    print(f'{key} --> {val}')

print(sorted_stats_en)