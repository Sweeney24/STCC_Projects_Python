#realeastate analyzer for Prof C's python class


#modified the previous assignments input validation to check for positive numbers
def getFloatInput(prompt): #this function is to check that inputs are positive numerical values
  while True: #loop for data validation
    try:
      uNumCheck = float(input(prompt)) #tries to turn the input into a float
      if uNumCheck > 0: #checks to make sure the number is positive
          return uNumCheck #returns the input as the product of this function
      else:
          print("please enter a positive number") #prompts if the input is less than 0.
    except ValueError: #if the input cannot turn into a float, this is called
      print("Invalid input. Please enter a valid number.")

def main():
    uRealEstateValues = [] #empty list to be populated by loops below
    while True:
        uSalesPrice = getFloatInput("Enter in the sales value")
        uRealEstateValues.append(uSalesPrice)
        uAnotherValue = input("Enter another value Y or N: ")
        while uAnotherValue.lower() not in ("y", "yes", "n", "no"):
            uAnotherValue = input("invalid entry, enter (y)es or (n)o")
        if uAnotherValue.lower() == "n":
            break


    uRealEstateValues.sort()

main()
