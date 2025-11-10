my_data = [11, 6, 8, 2, 22, 16, 25]

my_key = 42

# why does VS flag it?
outcome = yourSolution(my_data, my_key)

print("it's in position {outcome}")

def yourSolution(a, k):
    '''Can you speed up the Vanilla by deploying while?'''

    found = False

    n = len(a)

    # continue here...