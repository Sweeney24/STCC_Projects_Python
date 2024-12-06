#paint job estimator for Prof. C's python class

def getFloatInput(prompt): #this function is to check that inputs are positive numerical values
  while True:
    try: #this is not covered in the class text. I had to google this - it was driving me crazy trying to validate non-numerical values
      uNumCheck = float(input(prompt))
      return uNumCheck #returns the function value to variables outside the function.
    except ValueError:
      print("Invalid input. Please enter a valid number.")

fSquareFeetOfWall = (getFloatInput("Enter Square Feet of the Wall: "))
fPaintPrice = getFloatInput("Enter Paint Price: ")
fFeetPerGallonOfPaint = getFloatInput("Enter Feet per Gallon of Paint: ")
fLaborHoursPerGallon = getFloatInput("Enter Labor Hours per Gallon: ")
fPaintingLaborChargePerHour = getFloatInput("Enter Painting Labor charge per hour: ")

uValueList = [
    fSquareFeetOfWall,
    fPaintPrice,
    fFeetPerGallonOfPaint,
    fLaborHoursPerGallon,
    fPaintingLaborChargePerHour
]

print(uValueList)
