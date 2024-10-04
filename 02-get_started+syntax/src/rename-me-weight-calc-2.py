'''
The weight calculator project

Inform and amuse friends and family by computing their ideal weight under solid statistical rules!

a. ask for their height and current weight

b. compute the optimal weight with the Devine formula (go look)

c. print ideal weight and deviation

d. implement conditional computation by computing the Devine formula for M or F.
'''

# get started
# why use int()?
# why use double quotes?
current_weight = int(input("Hello, what's your weight in Kgs? "))

# height?
# copy and adapt the instruction above
height = int(input("and what's your height in inches? "))

# MOD 1
sex = input("Sex? (enter 'm' or 'f'): ")

# compute the target 
# https://www.bmi-calculator.net/ideal-weight-calculator/devine-formula/
# the formula is

if sex == 'm':
    # Men: Ideal Body Weight (kg) = 50 kg + 2.3 kg per inch over 5 feet.

    # not all height is used in the calculation, only that over 5 feet (= 60 inches):
    above_five_ft = height - 60

    ideal_weight = 50 + 2.3 * above_five_ft
else:
    # Women: Ideal Body Weight (kg) = 50 kg + 2.3 kg per inch over 5 feet.

    # not all height is used in the calculation, only that over 5 feet (= 60 inches):
    above_five_ft = height - 60

    ideal_weight = 50 + 2.3 * above_five_ft


# how's the patient doing?
residual = current_weight - ideal_weight

# print the answer
print(f"Well, for your height, ideal weight is {ideal_weight}. So, you are off target by {residual}")

'''
MOD 2:
add conditions to the 'if' part of the code so to obtain this behaviour:

- answerinng 'M' or 'F' works as well as 'm' or 'f', respectively

- answering any other keyboard character 
  will result in a 'diagnostic' message and termination
'''