





a = 'Thank you for trying my program!'
b = 'A Nickolas Reid production.'
# Attempt at a temperature calculator not that useful though :\
print '''Hello! This is my simple calculator to check to see how
your temperature is gaged! :)'''
print'''
'''
x = int(raw_input('''Please enter the temperature it is currently.
All temperatures are in celcius:'''))


if x >= 25:
    print 'very hot'
    print a
elif x >= 20:
    print 'Hot'
    print a
elif x >= 15:
    print 'very warm'
    print a
elif x >= 10:
    print 'warmer'
    print a
elif x >= 5:
    print 'warm'
    print a
elif x == 0:
    print 'freezing point'
    print a
else:
    print 'Get indoors!'
    print a
print'''
'''
x = int(raw_input("How would you rate my program out of 5?"))

if x <= 5:
    print 'Thank you for your feedback!'
else:
    print 'Error'
raw_input('Press enter to quit.')
