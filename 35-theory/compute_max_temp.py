temperaturelist = [27, 21, 16, 21, 19, 18, 19, 12, 15, 12]

maxchange = 0

trailer = temperaturelist[0]

for temp in temperaturelist:

  current_change = temp - trailer
  
  if abs(current_change) > maxchange:
    maxchange = abs(current_change) # a new max is found

  # we are finished with this value, assign it to the trailer
  trailer = temp

print(f'The maximum day-on-day increase has been {maxchange} degrees')