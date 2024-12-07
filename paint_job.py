#paint job estimator for Prof. C's python class
import math

def main():
    fSquareFeetOfWall = (getFloatInput("Enter Square Feet of the Wall: "))
    fPaintPrice = getFloatInput("Enter Paint Price: ")
    fFeetPerGallonOfPaint = getFloatInput("Enter the feet per gallon of paint: ")
    fLaborHoursPerGallon = getFloatInput("Enter Labor Hours per Gallon: ")
    fPaintingLaborChargePerHour = getFloatInput("Enter Painting Labor charge per hour: ")
    fStateSalesTax = getSalesTax(input("State the job is in: "))
    fUserName = input("Enter your last name: ")
    # getGallonsOfPaint(fSquareFeetOfWall, fFeetPerGallonOfPaint)
    Gallon_Of_Paint = getGallonsOfPaint(fSquareFeetOfWall, fFeetPerGallonOfPaint)
    fHours_of_labor = getLaborHours(fLaborHoursPerGallon, Gallon_Of_Paint)
    fLabor_cost = getLaborCost(fPaintingLaborChargePerHour, fFeetPerGallonOfPaint, fLaborHoursPerGallon,fSquareFeetOfWall)
    fPaint_Cost = getPaintCost(fPaintPrice, getGallonsOfPaint(fSquareFeetOfWall, fFeetPerGallonOfPaint))
    fTotalTax =  ((fLabor_cost + fPaint_Cost) * fStateSalesTax)
    fTotalCost = showCostEstimate(fLabor_cost, fPaint_Cost, fTotalTax)
    output_file(fUserName, Gallon_Of_Paint, fHours_of_labor, fPaint_Cost, fLabor_cost, fTotalTax, fTotalCost)
    print("Gallons of paint:" , Gallon_Of_Paint)
    print("Hours of labor: ", fHours_of_labor)
    print("Paint Cost: ${:.2f}".format(fPaint_Cost))
    print("Labor Charges: ${:.2f}".format(fLabor_cost))
    print("Tax: ${:.2f}".format(fTotalTax))
    print("Total Cost: ${:.2f}".format(fTotalCost))
    print(f"{fUserName}_PaintJobOutput.txt was created.")

def showCostEstimate(labor, paint, tax):
    return labor + paint + tax

def output_file(name, gallons, laborHours, paintCost, laborCost, totalTax, totalCost):
    file = open(f"{name}_PaintJobOutput.txt", "w")
    file.write(f"Gallons of paint: {gallons:}\n"
               f"Hours of labor: {laborHours:.2f}\n"
               f"Paint cost: ${paintCost:.2f}\n"
               f"Labor Charges: ${laborCost:.2f}\n"
               f"Tax: ${totalTax:.2f}\n"
               f"Total Cost: ${totalCost:.2f}\n")
    file.close()

def getSalesTax(prompt):
    fStates = (prompt)
    if fStates == "MA":
        fStateTax = .0625
    elif fStates == "CT":
        fStateTax = .06
    elif fStates == "RI":
        fStateTax = .07
    elif fStates == "ME":
        fStateTax = .085
    elif fStates == "VT":
        fStateTax = .06
    else:
        fStateTax = 0.0
    # print(fStateTax)
    return fStateTax

def getLaborCost(paint_labor_hour, feet_per_gallon,lab_hours_per_gallon, square_feet_of_wall):
    # fRealLaborCost = getLaborHours() * fPaintingLaborChargePerHour
    fRealLaborCost = getLaborHours(lab_hours_per_gallon, getGallonsOfPaint(square_feet_of_wall, feet_per_gallon)) * paint_labor_hour
    # print(float(fRealLaborCost))
    return fRealLaborCost

def getGallonsOfPaint(sq_ft_wall, feet_per_gallon):
    fRealGallons = sq_ft_wall / feet_per_gallon
    # fRealGallons = fSquareFeetOfWall / fFeetPerGallonOfPaint
    fRealGallons = math.ceil(fRealGallons)
    # print("gallons of paint: ", int(fRealGallons))
    return int(fRealGallons)

def getLaborHours(lab_hours_gal, gallons_of_paint):
    fRealLaborHour = lab_hours_gal * gallons_of_paint
    # fRealLaborHour = fLaborHoursPerGallon * getGallonsOfPaint()
    # print("Hours of Labor: ", float(fRealLaborHour))
    return float(fRealLaborHour)

def getPaintCost(paint_price, gallons_of_paint):
    fRealCostPaint = paint_price * gallons_of_paint
    # print("Cost of Paint : $ ", float(fRealCostPaint))
    return float(fRealCostPaint)


def getFloatInput(prompt): #this function is to check that inputs are positive numerical values
  while True: #loop for data validation
    try:
      uNumCheck = float(input(prompt)) #tries to turn the input into a float
      return uNumCheck #returns the function value to variables outside the function.
    except ValueError: #if the input cannot turn into a float, this is called
      print("Invalid input. Please enter a valid number.")


# fSquareFeetOfWall = (getFloatInput("Enter Square Feet of the Wall: "))
# fPaintPrice = getFloatInput("Enter Paint Price: ")
# fFeetPerGallonOfPaint = getFloatInput("Enter the feet per gallon of paint: ")
# fLaborHoursPerGallon = getFloatInput("Enter Labor Hours per Gallon: ")
# fPaintingLaborChargePerHour = getFloatInput("Enter Painting Labor charge per hour: ")



main()

