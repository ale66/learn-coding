'''
Find the maximum (resp. minimum) value change in a sequence

Algorithmic technique: the trailer variable

'''

temperatures_this_month = [27, 21, 16, 21, 19, 18, 19, 12, 15, 12]

'''
Question: 
which day of the month has seen 
the steepest temperature change (either increasing or decreasing)?
'''

# start with the minimum possible value
max_day_on_day_change = 0

# initialise the trailer variable
trailer = temperatures_this_month[0]

for temp in temperatures_this_month:

  current_change = temp - trailer
  
  if abs(current_change) > max_day_on_day_change:
  
    max_day_on_day_change = abs(current_change) # a new max is found

  # we are finished with this value, assign it to the trailer
  trailer = temp

print(f'The maximum day-on-day increase has been {max_day_on_day_change} degrees')


'''
Exercise: use the 'index()' method for lists to find out and print
on which day of the month we saw the steepest temperature change

Example:  temperatures_this_month.index(27) will return position 0

NB: this works correctly only if there are no repeated values in the list
'''

