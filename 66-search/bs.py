mylist = [11, 6, 8, 2, 22, 16, 25]

mylist.sort()

def bs(a, k):
    '''Simple Binary search implementation: a is a list of integers, k is a search key integer'''

    found = False

    n = len(a)

    # the boundaries of our search
    l = 0
    r = n

    while ((found == False) and (l < r)):

        mid = l + int((r-l)/2)
        
        '''print('New iteration!')
        print(f'l={l}, mid={mid}, r={r} and the segment now is {a[l:r]}')
        _ = input('Press enter to continue!')'''

        if k < a[mid]:
            r = mid 

        elif k > a[mid]:
            l = mid + 1

        else:
            found = True
            print('found in position ', mid)

    return found

# Verification: run the case seen in class:
print(bs(mylist, 15))

# Testing!
# comment out the 'step-by-step' part above before running


print(mylist)

print('Testing positive cases: values that are certainly there')
for v in mylist:
    print(f'testing {v}: {bs(mylist, v)}')

print('Testing negative cases: values that are certainly not there')
for v in mylist:
    print(f'testing {v+1}: {bs(mylist, v+1)}')

for bad_value in [-9, 0, 1, 100, 10000000]:
    print(f'testing {bad_value}: {bs(mylist, bad_value)}')
