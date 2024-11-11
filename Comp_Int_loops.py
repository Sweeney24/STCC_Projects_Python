#For Prof Candido's python class

#variables
uPrinciple = float(input('What is the starting principle: ')) #the users initial investment
while uPrinciple <= 0:
    print ('Please enter a positive number')
    uPrinciple = float(input('What is the starting principle: '))
uIntRate = float(input('What is the interest rate: ')) #the interest rate
while uIntRate <= 0:
    print ('Please enter a positive number')
    uIntRate = float(input('What is the annual interest rate: '))
uMonths = float(input('How many months to display: ')) #amount of months
while uMonths <= 0:
    print('Please enter a positive number')
    uMonths = float(input('How many months to display: '))
uGoal = float(input('What is the goal amount?'))
while uGoal <= 0:
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
uDisp_Month = 0

while uPrinciple < uGoal:
    # uMonths = uMonths + 1
    #uTime = (uMonths / 12)
    uDisp_Month += 1
    #uAccount_balance = uPrinciple * (1 + real_interest / 12) ** (12 * uTime)
    #uAccount_balance = uPrinciple * (1 + real_interest / 12) ** (12 * uMonths) #testing with umonths
    uPrinciple = uPrinciple * ( 1 + (real_interest / 12))

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