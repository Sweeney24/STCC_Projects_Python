#Temperature Converter Assignment for Prof. Candido's Python class

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


##conversion of F to C## This used to be just a F to C converter, but decided to nest if statements to be more concise.
#convert either C or F, depending on selection above
if tempNumber > 212 and (tempUnit == 'F' or tempUnit == 'f') or tempNumber > 100 and (tempUnit == 'C' or tempUnit == 'c'): #parentheses here force an accecpt of upper or lower case.
    if tempNumber > 212:
        print('Temp cannot be > 212') #this is exactly how it is written and demanded to be done in the assignment.
    else:
        print('Temp cannot be > 100') #this is exactly how it is written and demanded to be done in the assignment.
elif tempNumber <= 212 and (tempUnit == 'F' or tempUnit == 'f'): #parentheses here force an accecpt of f or F.
    convCelsius = (5.0/9) * (tempNumber - 32)
    print('The Celsius equivalent is: ', str(format(convCelsius, ".1f")))
elif tempNumber <=100 and (tempUnit == 'C' or tempUnit == 'c'):
    convFahrenheit = ((9.0/5.0) * tempNumber) + 32
    print('The Fahrenheit equivalent is: ', str(format(convFahrenheit, ".1f")))
#ending the F conversion here since Python will allow to exit without an ELSE. Unlike bash.

#BELOW HERE IS OLD CODE - DECIDED TO MAKE IT MORE STREAMLINED. TO BE IN LINE WITH RUBRIC.

#Conversion of C to F
# if tempNumber > 100 and (tempUnit == 'C' or tempUnit == 'c'): #same reason for parentheses as lines 22 and 24
#     print('Temp cannot be > 100')
# elif tempNumber <=100 and (tempUnit == 'C' or tempUnit == 'c'):
#     convFahrenheit = ((9.0/5.0) * tempNumber) + 32
#     print('The Fahrenheit equivalent is: ', str(format(convFahrenheit, ".1f")))
#ending C conversion here for same reason as line 27

