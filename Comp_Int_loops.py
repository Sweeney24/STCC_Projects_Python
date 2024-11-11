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
uMonths = float(input('How many months: ')) #amount of months
while uMonths <= 0:
    print('Please enter a positive number')
    uMonths = float(input('How many months: '))

uGoal = float(input('What is the goal amount?'))
while uGoal <= 0:
    print('Please enter a positive number')
    uGoal = float(input('What is the goal amount?'))

#convert to decimal
real_interest = uIntRate / 100

uTime = (uMonths / 12)

uAccount_balance = uPrinciple * (1 + real_interest / 12) ** (12 * uTime)
print(format(uAccount_balance, ".2f"))
uDisp_Month = 0
while uAccount_balance < uGoal:
    uMonths = uMonths + 1
    uTime = (uMonths / 12)

    for integer in range(1,13):
        uDisp_Month += 1
        uAccount_balance = uPrinciple * (1 + real_interest / 12) ** (12 * uTime)
        print(uDisp_Month, format(uAccount_balance, ".2f"))


#compute# following the order of operations.
#FinalValue = uPrinciple * (1 + real_interest / uMonth_int) ** (uMonth_int * uMonths)
#print('The expected value of your investment after', str(uMonths), 'months is','$',str(format(FinalValue,",.2f")))
