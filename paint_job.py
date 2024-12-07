#paint job estimator for Prof. C's python class
import math

def main(): # the main function, contains logic for how the program operates.
    #Other functions called here and saved to variables for inputting into further functions
    fSquareFeetOfWall = (getFloatInput("Enter Square Feet of the Wall: ")) #get the square feet
    fPaintPrice = getFloatInput("Enter Paint Price: ") #price of paint
    fFeetPerGallonOfPaint = getFloatInput("Enter the feet per gallon of paint: ")
    fLaborHoursPerGallon = getFloatInput("Enter Labor Hours per Gallon: ") #how many hours it takes to use a gallon
    fPaintingLaborChargePerHour = getFloatInput("Enter Painting Labor charge per hour: ") # labor charges
    fStateSalesTax = getSalesTax(input("State the job is in: ")) #for calculating sales tax
    fUserName = input("Enter your last name: ") #get the users last name
    # getGallonsOfPaint(fSquareFeetOfWall, fFeetPerGallonOfPaint)
    Gallon_Of_Paint = getGallonsOfPaint(fSquareFeetOfWall, fFeetPerGallonOfPaint)#variable for storing function estimating gallons of paint needed
    fHours_of_labor = getLaborHours(fLaborHoursPerGallon, Gallon_Of_Paint) # variable to store the hours of labor
    fLabor_cost = getLaborCost(fPaintingLaborChargePerHour, fFeetPerGallonOfPaint, fLaborHoursPerGallon,fSquareFeetOfWall) #variable to store the labor cost
    fPaint_Cost = getPaintCost(fPaintPrice, getGallonsOfPaint(fSquareFeetOfWall, fFeetPerGallonOfPaint)) # variable to store the estimated cost of paint for the job
    fTotalTax =  ((fLabor_cost + fPaint_Cost) * fStateSalesTax) # Variable to store the calculated tax amount
    fTotalCost = showCostEstimate(fLabor_cost, fPaint_Cost, fTotalTax, Gallon_Of_Paint,fHours_of_labor, fPaint_Cost,
                                  fLabor_cost, fTotalTax, fUserName) #variable to store the output of the cost estimator function - really only saves the labor cost, paint cost and tax amount and sums them.
    output_file(fUserName, Gallon_Of_Paint, fHours_of_labor, fPaint_Cost, fLabor_cost, fTotalTax, fTotalCost) #calling function to output the info to a text file.

    # print("Gallons of paint:" , Gallon_Of_Paint)   These have been moved to the cost estimator function.
    # print("Hours of labor: ", fHours_of_labor)
    # print("Paint Cost: ${:.2f}".format(fPaint_Cost))
    # print("Labor Charges: ${:.2f}".format(fLabor_cost))
    # print("Tax: ${:.2f}".format(fTotalTax))
    # print("Total Cost: ${:.2f}".format(fTotalCost))
    # print(f"{fUserName}_PaintJobOutput.txt was created.")

def showCostEstimate(labor, paint, tax, gallons, laborHours, paintCost, laborCost, totalTax, name):
    #function to calculate total cost of job. Also prints out the calculated values of the other functions
    totalCost = labor + paint + tax
    print("{:<15} {:>18}".format("Gallons of paint:", gallons))
    print("{:<15} {:>20.2f}".format("Hours of labor:", laborHours))
    print("{:<15} {:>20}".format("Paint Cost:", f"${paintCost:.2f}"))
    print("{:<15} {:>20}".format("Labor Charges:", f"${laborCost:.2f}"))
    print("{:<15} {:>20}".format("Tax:", f"${totalTax:.2f}"))
    print("{:<15} {:>20}".format("Total Cost:", f"${totalCost:.2f}"))
    return totalCost

def output_file(name, gallons, laborHours, paintCost, laborCost, totalTax, totalCost): #creates the output file
    # print("Gallons of paint:" , gallons)
    # print("Hours of labor: ", laborHours)
    # print("Paint Cost: ${:.2f}".format(paintCost))
    # print("Labor Charges: ${:.2f}".format(laborCost))
    # print("Tax: ${:.2f}".format(totalTax))
    # print("Total Cost: ${:.2f}".format(totalCost))
    print(f"{name}_PaintJobOutput.txt was created.")
    file = open(f"{name}_PaintJobOutput.txt", "w")
    file.write(f"{'Gallons of paint:':<20} {gallons:>20}\n"
               f"{'Hours of labor:':<20} {laborHours:>20.2f}\n"
               f"{'Paint cost:':<20} {f'${paintCost:.2f}':>20}\n"
               f"{'Labor Charges:':<20} {f'${laborCost:.2f}':>20}\n"
               f"{'Tax:':<20} {f'${totalTax:.2f}':>20}\n"
               f"{'Total Cost:':<20} {f'${totalCost:.2f}':>20}\n")
    file.close()

def getSalesTax(prompt): #if logic for sales tax. NH omitted since the value is equal to no state being input.
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

def getLaborCost(paint_labor_hour, feet_per_gallon,lab_hours_per_gallon, square_feet_of_wall): #get the total labor cost
    # fRealLaborCost = getLaborHours() * fPaintingLaborChargePerHour
    #math to calculate the total labor cost, calls the function to get total gallons.
    fRealLaborCost = getLaborHours(lab_hours_per_gallon, getGallonsOfPaint(square_feet_of_wall, feet_per_gallon)) * paint_labor_hour
    # print(float(fRealLaborCost))
    return fRealLaborCost

def getGallonsOfPaint(sq_ft_wall, feet_per_gallon): #get the total gallons needed for the project
    fRealGallons = sq_ft_wall / feet_per_gallon #math to calculate total gallons needed
    # fRealGallons = fSquareFeetOfWall / fFeetPerGallonOfPaint
    fRealGallons = math.ceil(fRealGallons) #math function that rounds up
    # print("gallons of paint: ", int(fRealGallons))
    return int(fRealGallons) #returning integer

def getLaborHours(lab_hours_gal, gallons_of_paint): #gets the total labor hours and returns it
    fRealLaborHour = lab_hours_gal * gallons_of_paint #math to calculate labor hours
    # fRealLaborHour = fLaborHoursPerGallon * getGallonsOfPaint()
    # print("Hours of Labor: ", float(fRealLaborHour))
    return float(fRealLaborHour)

def getPaintCost(paint_price, gallons_of_paint): #gets the total paint cost and returns it.
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

main()


#Old variables - moved into main function


# fSquareFeetOfWall = (getFloatInput("Enter Square Feet of the Wall: "))
# fPaintPrice = getFloatInput("Enter Paint Price: ")
# fFeetPerGallonOfPaint = getFloatInput("Enter the feet per gallon of paint: ")
# fLaborHoursPerGallon = getFloatInput("Enter Labor Hours per Gallon: ")
# fPaintingLaborChargePerHour = getFloatInput("Enter Painting Labor charge per hour: ")





