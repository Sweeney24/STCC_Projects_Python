#paint job estimator for Prof. C's python class
import math

def main():

    getGallonsOfPaint()
    getLaborHours()
    getLaborCost()
    getPaintCost()
    getSalesTax("State the job is in: ")

def getSalesTax(prompt):
    fStates = input(prompt)
    if fStates == "MA":
        fStateTax = .06
    elif fStates == "CT":
        fStateTax = .0625
    elif fStates == "RI":
        fStateTax = .07
    elif fStates == "ME":
        fStateTax = .085
    elif fStates == "VT":
        fStateTax = .06
    else:
        fStateTax = 0.0
    print(fStateTax)
    return fStateTax

def getLaborCost():
    fRealLaborCost = getLaborHours() * fPaintingLaborChargePerHour
    print(float(fRealLaborCost))

    return fRealLaborCost

def getGallonsOfPaint():
    fRealGallons = fSquareFeetOfWall / fFeetPerGallonOfPaint
    fRealGallons = math.ceil(fRealGallons)
    # print(int(fRealGallons))
    return int(fRealGallons)

def getLaborHours():
    fRealLaborHour = fLaborHoursPerGallon * getGallonsOfPaint()
    print("Labor Hours: ", float(fRealLaborHour))
    return float(fRealLaborHour)

def getPaintCost():
    fRealCostPaint = fPaintPrice * getGallonsOfPaint()
    print(float(fRealCostPaint))
    return float(fRealCostPaint)

def getFloatInput(prompt): #this function is to check that inputs are positive numerical values
  while True:
    try: #this is not covered in the class text. I had to google this - it was driving me crazy trying to validate non-numerical values
      uNumCheck = float(input(prompt))
      return uNumCheck #returns the function value to variables outside the function.
    except ValueError:
      print("Invalid input. Please enter a valid number.")


fSquareFeetOfWall = (getFloatInput("Enter Square Feet of the Wall: "))
fPaintPrice = getFloatInput("Enter Paint Price: ")
fFeetPerGallonOfPaint = getFloatInput("Enter the feet per gallon of paint: ")
fLaborHoursPerGallon = getFloatInput("Enter Labor Hours per Gallon: ")
fPaintingLaborChargePerHour = getFloatInput("Enter Painting Labor charge per hour: ")

MA = .06
CT = .0625
ME = .085
NH = .0
RI = .07
VT = .06

main()

# fUserState = input("Please enter the state of the job") #the state location of the job
# fUserLname = input("Please enter your surname name")

# uValueList = [
#     fSquareFeetOfWall,
#     fPaintPrice,
#     fFeetPerGallonOfPaint,
#     fLaborHoursPerGallon,
#     fPaintingLaborChargePerHour
# ]
#
# print(uValueList)

# A painting company has determined that for every 112 square
# feet of wall space, one gallon of paint and eight hours of labor
# will be required. The company charges $35.00 per hour for
# labor. Write a program that asks the user to enter the square
# feet of wall space to be painted and the price of the paint per
# gallon