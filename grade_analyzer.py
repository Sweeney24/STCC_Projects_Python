#Grade analyzer for Prof. Candido's python class

#ask the user the grades to be analyzed
uFirst_test = float(input('First test score: '))
uSec_test = float(input('Second test score: '))
uThird_test = float(input('Third test score: '))
uFourth_test = float(input('Fourth test score: '))
#ask user if dropping lowest score
uDrop_test = input('Drop the lowest test score? Y or N: ')
NO_DROP_TEST = (uFirst_test + uSec_test + uThird_test + uFourth_test) / 4 #Constant here as there is no need for
                                                                         # additional logic
calc_Drop_uFirst = (uSec_test + uThird_test + uFourth_test) / 3
calc_Drop_uSecond = (uFirst_test + uThird_test + uFourth_test) / 3
calc_Drop_uThird = (uFirst_test + uSec_test + uFourth_test) / 3
calc_Drop_uFourth =  (uFirst_test + uSec_test + uThird_test) / 3


#if elif else logic
if uDrop_test == 'Y' or uDrop_test == 'y':
    if uFirst_test <= uSec_test and uFirst_test <= uThird_test and uFirst_test <= uFourth_test:
        print(calc_Drop_uFirst)
    elif uSec_test <= uThird_test and uSec_test <= uFourth_test and uSec_test <= uFirst_test:
        print(calc_Drop_uSecond)
    elif uThird_test <= uFourth_test and uThird_test <= uFirst_test and uThird_test <= uSec_test:
        print(calc_Drop_uThird)
    else:
        print(calc_Drop_uFourth)
else:
    print(NO_DROP_TEST)