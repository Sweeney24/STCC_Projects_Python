#Grade analyzer for Prof. Candido's python class
#ask for whom we are grading
uName = input('What is the name of the person we are calculating grades for? ')
#ask the user the grades to be analyzed
uFirst_test = int(input('First test score: '))
uSec_test = int(input('Second test score: '))
uThird_test = int(input('Third test score: '))
uFourth_test = int(input('Fourth test score: '))

uDrop_test = input('Drop the lowest test score? Y or N: ') #ask user if dropping lowest score
uMin = 0  # variable that changes based on lowest grade

NO_DROP_TEST = (uFirst_test + uSec_test + uThird_test + uFourth_test) / 4 #Constant

if uFirst_test >=0 and uSec_test >=0 and uThird_test >=0 and uFourth_test >=0:
    if uDrop_test != 'Y' and uDrop_test != 'N' and uDrop_test != 'y' and uDrop_test != 'n':
        print('Please choose Y or N')
        exit()
    elif uDrop_test == 'Y' or uDrop_test == 'y':
        if uFirst_test < uSec_test:
            if uFirst_test < uThird_test:
                if uFirst_test < uFourth_test:
                        uMin = uFirst_test
                        #print("first should be min",YES_DROP_TEST)
                else:
                        uMin = uFourth_test
                        #print("Fourth min",YES_DROP_TEST)
            else:
                if uThird_test < uFourth_test:
                        uMin = uThird_test
                        #print("Third min",YES_DROP_TEST)
                else:
                        uMin = uFourth_test
                        #print("Fourth min",YES_DROP_TEST)
        else:
            if uSec_test < uThird_test:
                if uSec_test < uFourth_test:
                        uMin = uSec_test
                        #print("Second min",YES_DROP_TEST)
                else:
                        uMin = uFourth_test
                        #print("Fourth min",YES_DROP_TEST)
            else:
                if uThird_test < uFourth_test:
                        uMin = uThird_test
                        #print("Third min",YES_DROP_TEST)
                else:
                        uMin = uFourth_test
                        #print(uMin,"Fourth min",YES_DROP_TEST)
            YES_DROP_TEST = (uFirst_test + uSec_test + uThird_test + uFourth_test - uMin) / 3  # Constant here
            print(uName,' received a ',format(YES_DROP_TEST, ".1f"))
    else:
        print("no",NO_DROP_TEST)
else:
    print('Test score cannot be less than 0')
    exit()

#if elif else statements for grade letter.
if YES_DROP_TEST >= 97.0 or NO_DROP_TEST >= 97.0:
    print('Letter grade average is A+')
elif YES_DROP_TEST >= 94.0 or NO_DROP_TEST >= 94.0:
    print('Letter grade average is A')
elif YES_DROP_TEST >= 90.0 or NO_DROP_TEST >= 90.0:
    print('Letter grade average is A-')
elif YES_DROP_TEST >= 87.0 or NO_DROP_TEST >= 87.0:
    print('Letter grade average is B+')
elif YES_DROP_TEST >= 84.0 or NO_DROP_TEST >= 84.0:
    print('Letter grade average is B')
elif YES_DROP_TEST >= 80.0 or NO_DROP_TEST >= 80.0:
    print('Letter grade average is B-')
elif YES_DROP_TEST >= 77.0 or NO_DROP_TEST >= 77.0:
    print('Letter grade average is C+')
elif YES_DROP_TEST >= 74.0 or NO_DROP_TEST >= 74.0:
    print('Letter grade average is C')
elif YES_DROP_TEST >= 70.0 or NO_DROP_TEST >= 70.0:
    print('Letter grade average is C-')
elif YES_DROP_TEST >= 67.0 or NO_DROP_TEST >= 67.0:
    print('Letter grade average is D+')
elif YES_DROP_TEST >= 64.0 or NO_DROP_TEST >= 64.0:
    print('Letter grade average is D')
elif YES_DROP_TEST >= 60.0 or NO_DROP_TEST >= 60.0:
    print('Letter grade average is D-')
else:
    print('Letter grade average is F')




# calc_Drop_uFirst = (uSec_test + uThird_test + uFourth_test) / 3
# calc_Drop_uSecond = (uFirst_test + uThird_test + uFourth_test) / 3
# calc_Drop_uThird = (uFirst_test + uSec_test + uFourth_test) / 3
# calc_Drop_uFourth =  (uFirst_test + uSec_test + uThird_test) / 3

# #if elif else logic
# if uDrop_test == 'Y' or uDrop_test == 'y':
#     if uFirst_test <= uSec_test and uFirst_test <= uThird_test and uFirst_test <= uFourth_test:
#         print(calc_Drop_uFirst)
#     elif uSec_test <= uThird_test and uSec_test <= uFourth_test and uSec_test <= uFirst_test:
#         print(calc_Drop_uSecond)
#     elif uThird_test <= uFourth_test and uThird_test <= uFirst_test and uThird_test <= uSec_test:
#         print(calc_Drop_uThird)
#     else:
#         print(calc_Drop_uFourth)
# else:
#     print(NO_DROP_TEST)