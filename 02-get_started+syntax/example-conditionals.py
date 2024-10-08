LIMIT=32

temp = int(input('Hey, what is the temperature today?'))

if temp > LIMIT:
    # Notice the indentation
    print('Go cover the tomatoes!')
else:
    print('Temperature is alright today for growing tomatoes on your terrace!')


if temp > LIMIT:
    # Notice the indentation
    print('Go cover the tomatoes!')
elif temp < LIMIT:
    print('Temperature is alright today for growing tomatoes on your terrace!')
else:
    print('The limit temperature has been reached, prepare for emergency tomato covering!')