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
    # write it by yourself...Ok
    continue


# make the change permanent to the list
howmany = len(teams)

for i in range(howmany):
    # first I index the list, then I index the single string within
    teams[i] = teams[i][0:-3]


#Thomas
fruits = ['apple', 'banana', 'cherry', 'blackcurrant']
for fruit in fruits:
    if fruit == 'banana':
        continue
    print (fruit)


# Filippo
fruits = ['apple', 'banana', 'cherry', 'blackcurrant']
len(fruits)

for f in fruits: # fruit begins by 'f', not by 'i', just saying
    if f != "banana":
        print(f)
    

# Connie
fruits = ['apple', 'cherry', 'banana', ''blackcurrant'] # you're missing quotes around balckcurrant
if i

# Sara
]
fruits = ['apple', 'cherry', 'banana', 'blackcurrant']


for f in fruits:
    if f != "banana": # the ':' must be the last character of the line

# Riccardo

fruits = ['apple', 'banana', 'cherry', 'blackcurrant']

for f in fruits:  # call it 'f' for  fruits?
    if f != "banana":
        print(f)


#Giada == Anna
fruits = ['apple', 'banana', 'cherry', 'blackcurrant']
 
for f in fruits:   
    if f == "banana":
        continue
    else:
        print('Good for you - Olivia Rodrigo said')



        
#Giulia 
fruits = ['apple', 'banana', 'cherry', 'blackcurrant']
for f in fruits:
    if f == 'banana':
        continue
    else:
        print('Good for you: ', f)



#Jeppe
fruits = ['apple', 'banana', 'cherry', 'blackcurrant']
for i in fruits:
    if i == 'banana':
        continue
    else:
        print(i)
    

#Mathilde 
fruits = ['apple', 'banana', 'cherry', 'blackcurrant']
for f in fruits: 
    if f == 'banana':
        continue 
    else: 
        print (f)
    


# Ale66
for f in fruits:
    if f == 'banana':
        continue
    else:
        print('Good for you: ', f)
        
        
        

#wen yu
fruit=['apple','banana','cherry','blackcurrant']
for i in fruit: # why should a fruit be called 'l'???
    if i =='banana':
        print(i)
        break
        
 

#Enrico
fruits=['apple','banana','cherry','blackcurrant']
for f in fruits: 
    if f == 'banana' # you need ':' here...
       continue
       print('fruits')

