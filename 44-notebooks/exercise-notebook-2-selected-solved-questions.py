# ==============================================================
# Model solution for question 8 of exercise set 2
# Uncomment to run

'''
list_names = ['Juliet', 'John', 'Jack', 'Joy', 'Jim', 'Josh', 'Julia']

name1 = input('Please enter your name: ')

found = False

for name in list_names:
    if name == name1:
        found = True


if found == True:
    print('Congratulations, you are registered already!')

else:
    print("Sorry, we don't have your name in the list")
'''

# ==============================================================
# Model solution for question 15-b of exercise set 2
# This version represents a slight generalization to arbitrary input prefixes
# Uncomment to run

list = ['car', 'cat', 'spot', 'talk', 'way', 'code', 
        'dog', 'fly', 'fun', 'road', 'house', 'duck', 
        'chew', 'list', 'train']

n = len(list)

prefix = input('Type the beginning of the word: ')
# original version
# prefix = 'ca'

l = len(prefix)

found =  False

# with 'for' iteration:
for word in list:
    if word[ :l] == prefix:
        found = True

'''
# for reference:
# with 'while' iteration
i=0  

while i < n:
    # if the beginning of the word coincides with the prefix
    if list[i][ :l] == prefix:
        found = True
    
    #increment
    i += 1
'''

if found == True:
    print('A word with this prefix exists already!')

else:
    print("Sorry, we don't have any words with such prefix!")
