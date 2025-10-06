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

'''
Exercise 1 (simple):

Obtain the height in inches of the patient
copy and adapt the instruction above

define variable 'height'
'''


# body type?
body = input("Great, and body type (male/female)? ")


# compute the target weight now
if body == 'male':
    ideal_weight = 50 + 2.3 * (height - 60)
else:
    ideal_weight = 45.5 + 2.3 * (height - 60)


'''
Exercise 2 (challenge):

Calculate the weight to be lost (or gained) in order to reach ideal weight

E.g., negative result would mean that the user whould loose that much weight
'''
