#hello Bogdana
# In-class work


# assigned to Bogdana
# Print a string vertically (one character per line) in reverse order

mystring = 'Crystal Palace FC'

newstring = reversed(mystring)

for i in newstring:
    print(i)


    
# assigned to Sundeep
# print out the single string containing the names of each fruit without spaces

fruitlist = ['apple', 'banana', 'cherry']
'''
print(fruitlist)

print(fruitlist[0])

print(fruitlist[1])

print(fruitlist[2])
'''

print(f'{fruitlist[0]}{fruitlist[1]}{fruitlist[2]}')



# assigned to Elisabeth
# Alter lists: add newfruit to fruitlist only if not present already 
'''
newfruit = 'orange'
'''

teams = ['Chelsea FC', 'Arsenal FC', 'Crystal Palace FC', 'West Ham FC']

howmany = len(teams)


# assigned to Sam
# print them as they are
for single_team in teams:
    print(single_team)
    # write here
    continue


# assigned to Elisabeth
# print w/o the ' FC' part!
for single_team in teams:
    # write here
    if single_team == "FC":
       print("w/o")
    continue

# assigned to Sundeep
# drop the FC part from the list permanently
for i in range(howmany):
    # write here
    continue

# assigned to Sam
# Challenge: remove duplicates from a list
too_many = ['Chelsea FC', 'Arsenal FC', 'Crystal Palace FC', 'West Ham FC', 'Arsenal FC']

temp_list = []

for team in too_many:
    if team in temp_list:
        pass
    else:
        temp_list.append(team)
print(team)
