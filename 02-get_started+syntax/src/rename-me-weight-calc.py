'''
The weight calculator project

Inform and amuse friends and family by computing their ideal weight under solid statistical rules!

a. Ask for their height and current weight

b. compute the optimal weight with the Devine formula (go look)

c. print ideal weight and deviation

d. implement conditional computation by computing the Devine formula for M or F.
'''

# get started
# why use int()?
# why use double quotes?
current_weight = int(input("Hello, what's your weight? "))

# height?
# copy and adapt the instruction above
height = int(input("Thanks, and what's your height in inches?"))

body = input("Great, and body type (male/female?")
# compute the target 

if body == 'male':
    ideal_weight = 50 + 2.3 * (height - 60)
else:
    ideal_weight = 45.5 + 2.3 * (height - 60)



# continue here...

residual = ideal_weight - current_weight

# print the answer
