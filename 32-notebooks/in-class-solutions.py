# ============== Exercise 15.a ===================================
# find occurences of the value of CITY inside text

text = '''Two households, both alike in dignity, 
          In fair Verona, where we lay our scene, 
          From ancient grudge break to new mutiny, 
          Where civil blood makes civil hands unclean.
       '''

CITY = 'Verona'

if CITY in text:
    print(f'The city of {CITY} is found in text')

# Now, try without using 'in'


'''
Visualisation of the sliding pattern solution:

Two households, both alike in dignity,
??????
Verona
-Verona
--Verona
---Verona
----Verona
-----Verona
------Verona
-------Verona
'''

n = len(text)

m = len(CITY)

no_of_possible_tests = n - m + 1

print(f'We need {no_of_possible_tests} separated tests!')

for i in range(no_of_possible_tests):

    print(text[i : i+m])

    if text[i : i+m] == CITY:

        print(f'Found {CITY} in position {i} of text!')
        break



# ============== Exercise 15.b ===================================

'''
Write a program to create the following list of words *car, cat, spot, talk, way, code*

*   Search and print for the words starting with *ca*, such as *car, cat, ...*.

*   In case that there are not results, print 'No results'.
'''

my_words =  ['car', 'cat', 'spot', 'talk', 'way']

my_words.append('code')

PATTERN = 'ca'

for w in my_words:
    continue

