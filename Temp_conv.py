#Temperature Converter Assignment for Prof. Candido's Python class
from idlelib.run import exit_now

#first write out a welcome message WITH my name
print("Hello, and welcome to the temperature converter! \nMy name is Andrew and I'll be your guide to converting \
temperature from Fahrenheit to Celsius. Or Celsius to Fahrenheit")

#Get the numerical value the user wants converted
tempNumber = float(input('Enter the temperature you wish to be converted: '))
#Get the unit that the user wants to convert to
tempUnit = input('Is this Fahrenheit or Celsius? Enter F or C: ')
#check to see if user's input is acceptable
if tempUnit == 'F' or tempUnit == 'f': #adding option for lowercase because why not.
    print('You have selected Fahrenheit')
elif tempUnit == 'C' or tempUnit == 'c':
    print('You have selected Celsius')
else:
    print('Please Enter either F or C')
    exit_now

#conversion of F to C
if tempNumber > 212 and (tempUnit == 'F' or tempUnit == 'f'): #parentheses here force an accecpt of upper or lower case.
    print('Temp cannot be > 212') #this is exactly how it is written and demanded to be done in the assignment.
elif tempNumber <= 212 and (tempUnit == 'F' or tempUnit == 'f'): #parentheses here force an accecpt of f or F.
    convCelsius = (5.0/9) * (tempNumber - 32)
    print('The Celsius equivalent is: ', str(format(convCelsius, ".1f")))
#ending the F conversion here since Python will allow to exit without an ELSE. Unlike bash.

#Conversion of C to F
if tempNumber > 100 and (tempUnit == 'C' or tempUnit == 'c'): #same reason for parentheses as lines 22 and 24
    print('Temp cannot be > 100')
elif tempNumber <=100 and (tempUnit == 'C' or tempUnit == 'c'):
    convFahrenheit = ((9.0/5.0) * tempNumber) + 32
    print('The Fahrenheit equivalent is: ', str(format(convFahrenheit, ".1f")))
#ending C conversion here for same reason as line 27

