#compound interest coding assignment for Prof. Candido's python class.

#variables
uPrinciple = float(input('What is the starting principle: ')) #the users initial investment
uIntRate = float(input('What is the annual interest rate: ')) #the interest rate
uCompound = float(input('How many times per year is the interest compounded: ')) #how often the interest compounds
uYears = float(input('How many years will the account earn interest: ')) #how long the user will invest

#convert to decimal
real_interest = uIntRate / 100

#compute# following the order of operations.
FinalValue = uPrinciple * (1 + real_interest / uCompound) ** (uCompound * uYears)

#print out expected investment. Converting the float of the amount of year to a string.
# Also converting the final value to a string for easier formating.
print('The expected value of your investment after', str(uYears), 'years is','$',str(format(FinalValue,"$,.2f")))