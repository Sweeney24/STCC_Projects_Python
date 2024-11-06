#Grade analyzer for Prof. Candido's python class

#ask the user the grades to be analyzed
uFirst_test = int(input('First test score: '))
uSec_test = int(input('Second test score: '))
uThird_test = int(input('Third test score: '))
uFourth_test = int(input('Fourth test score: '))
#ask user if dropping lowest score
uDrop_test = input('Drop the lowest test score? Y or N: ')
uMin = 0
NO_DROP_TEST = (uFirst_test + uSec_test + uThird_test + uFourth_test) / 4 #Constant here as there is no need for additional logic
YES_DROP_TEST = (uFirst_test + uSec_test + uThird_test + uFourth_test - uMin) / 3 #Constant here

if uDrop_test == 'Y' or uDrop_test == 'y':
    if uFirst_test < uSec_test:
        if uFirst_test < uThird_test:
            if uFirst_test < uFourth_test:
                uMin = uFirst_test
                print("first should be min",YES_DROP_TEST)
            else:
                uMin = uFourth_test
                print("Fourth min",YES_DROP_TEST)
        else:
            if uThird_test < uFourth_test:
                uMin = uThird_test
                print("Third min",YES_DROP_TEST)
            else:
                uMin = uFourth_test
                print("Fourth min",YES_DROP_TEST)
    else:
        if uSec_test < uThird_test:
            if uSec_test < uFourth_test:
                uMin = uSec_test
                print("Second min",YES_DROP_TEST)
            else:
                uMin = uFourth_test
                print("Fourth min",YES_DROP_TEST)
        else:
            if uThird_test < uFourth_test:
                uMin = uThird_test
                print("Third min",YES_DROP_TEST)
            else:
                uMin = uFourth_test
                print(uMin,"Fourth min",YES_DROP_TEST)
else:
    print("no",NO_DROP_TEST)


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