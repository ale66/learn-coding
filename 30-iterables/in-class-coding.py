# In-class work

# Use this to experiment in class with 
# the Microsoft Live Share extension:
# https://visualstudio.microsoft.com/services/live-share/

# TO DO: remove the triple quotes (''') in order to execute

'''''''''''''''
# assigned to: Julie, Sofus and Ida
# Print a string vertically (one character per line) in reverse order
'''
mystring = 'Crystal Palace FC'

for letter in mystring:
    print(letter[-1:-18])
#option two?  
n = -1
for letter in mystring:
    print(mystring(n))
    n=n-1




# assigned to Arianna, Lorenzo
# print out the single string containing the names of each fruit without spaces
fruitlist = ('apple', 'banana', 'cherry')
print(''.join(fruitlist))




'''
# assigned to christine, Villads, Mille
# Alter lists: add newfruit to fruitlist only if not present already 

another_fruitlist = ['apple' , 'banana' , 'cherry']


newfruit = 'orange'
for x in another_fruitlist:
    if x == newfruit:
        print('already present')
        break
    
else:
    print('not present')
    another_fruitlist.append(newfruit)
print(another_fruitlist)

'''


teams = ['Chelsea FC', 'Arsenal FC', 'Crystal Palace FC', 'West Ham FC']

howmany = len(teams)


# not assigned
# print them as they are
for single_team in teams:
    # write here
    continue

# assigned to Alejandra & Paula
# print w/o the ' FC' part!
    print teams[-1:2]
    .remove (' FC')
    
for single_team in teams:
    # write here
    continue

'''
Model solution
'''

my_teams = ['Chelsea FC', 'Arsenal FC', 'Crystal Palace FC', 'West Ham FC']

for t in my_teams:
    print(t[0:-3])









# assigned to Daniele
# drop the FC part from the list permanently
for i in range(howmany):
    teams[i] = teams[i].replace(' FC', '')
    print(teams)

# assigned to
# Challenge: remove duplicates from a list
too_many = ['Chelsea FC', 'Arsenal FC', 'Crystal Palace FC', 'West Ham FC', 'Arsenal FC']
