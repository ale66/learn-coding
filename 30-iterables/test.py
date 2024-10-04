'''
fruitlist = ["apple", "banana", "cherry"]

print(fruitlist)

newfruit = 'orange'

fruitlist[1] = newfruit

print(fruitlist)
'''

'''
mystring = 'Alessandro'

for character in mystring:
    print(character)
'''

teams = ['Chelsea FC', 'Arsenal FC', 'Crystal Palace FC', 'West Ham FC']

# print them as they are
for single_team in teams:
    print(single_team)

# print w/o the ' FC' part!
for single_team in teams:
    print(single_team[0:-3])

# make the change permanent to the list
howmany = len(teams)

for i in range(howmany):
    # write it by yourself...
    continue


# make the change permanent to the list
howmany = len(teams)

for i in range(howmany):
    # first I index the list, then I index the single string within
    teams[i] = teams[i][0:-3]

