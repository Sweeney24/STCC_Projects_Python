#For Prof Candido's python class

#variables
uPrinciple = float(input('What is the starting principle: ')) #the users initial investment
while uPrinciple < 0: # find the starting principle - only accepts greater than 0
    print ('Please enter a positive number')
    uPrinciple = float(input('What is the starting principle: '))
uIntRate = float(input('What is the interest rate: ')) #the interest rate as a float
while uIntRate < 0: # find the yearly interest rate - only accepts positive numbers
    print ('Please enter a positive number')
    uIntRate = float(input('What is the annual interest rate: '))
uMonths = float(input('How many months to display: '))
while uMonths < 0: #find the amount of months to display as a float, greater than 0
    print('Please enter a positive number')
    uMonths = float(input('How many months to display: '))
uGoal = float(input('What is the goal amount?'))
while uGoal <= 0: #find the goal the user wants - greater than or equal to 0
    print('Please enter a positive number')
    uGoal = float(input('What is the goal amount?'))

#convert to decimal
real_interest = float(uIntRate / 100) # get decimal for percent interest

#uTime = (uMonths / 12) # the decimal interest of the goal # this is incorrect
# print (uTime)
#


#uAccount_balance = uPrinciple * (1 + real_interest / 12) ** (12 * uTime) #incorrect logic
#uAccount_balance = uPrinciple * (1 + real_interest / 12) ** (12 * uMonths) #testing with umonths
#print(format(uAccount_balance, ".2f"))
uDisp_Month = 0 #starting a variable at 0 for iteration purposes

while uPrinciple < uGoal:
    # uMonths = uMonths + 1
    #uTime = (uMonths / 12) #misunderstood and was trying to use the "months to display"  to calculate
    uDisp_Month += 1 #increasing the value of a variable for iteration
    #uAccount_balance = uPrinciple * (1 + real_interest / 12) ** (12 * uTime) # old and incorrect
    #uAccount_balance = uPrinciple * (1 + real_interest / 12) ** (12 * uMonths) #testing with umonths
    uPrinciple = uPrinciple * ( 1 + (real_interest / 12)) #math to get monthly interest increase

    #uMonths = uMonths + 1
    if uDisp_Month <= uMonths:
        print('Month', uDisp_Month,': $', format(uPrinciple, '.2f') )
    # print('Month', uDisp_Month, format(uPrinciple, ".2f"))

print('It will take ', str(uDisp_Month), ' months to reach your goal of $', str(format(uGoal, ",.2f")))
#
#
# #compute# following the order of operations.
# #FinalValue = uPrinciple * (1 + real_interest / uMonth_int) ** (uMonth_int * uMonths)
# #print('The expected value of your investment after', str(uMonths), 'months is','$',str(format(FinalValue,",.2f")))
#