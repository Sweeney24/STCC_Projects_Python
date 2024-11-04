#Temperature Converter Assignment for Prof. Candido's Python class
from idlelib.run import exit_now

#first write out a welcome message WITH my name
print("Hello, and welcome to the temperature converter! \nMy name is Andrew and I'll be your guide to converting \
temperature from Fahrenheit to Celsius. Or Celsius to Fahrenheit")

#Get the numerical value the user wants coverted
tempNumber = float(input('Enter the temperature you wish to be converted: '))
#Get the unit that the user wants to convert to
tempUnit = input('Is this Fahrenheit or Celsius? Enter F or C: ')
#check to see if user's input is acceptable
if tempUnit == 'F' or tempUnit == 'f':
    print('You have selected Fahrenheit')
elif tempUnit == 'C' or tempUnit == 'c':
    print('You have selected Celsius')
else:
    print('Please Enter either F or C')
    exit_now

#Conversion equations


