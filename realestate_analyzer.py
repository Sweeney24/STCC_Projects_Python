#realeastate analyzer for Prof C's python class

def getFloatInput(prompt): #this function is to check that inputs are positive numerical values
  while True: #loop for data validation
    try:
      uNumCheck = float(input(prompt)) #tries to turn the input into a float
      return uNumCheck #returns the function value to variables outside the function.
    except ValueError: #if the input cannot turn into a float, this is called
      print("Invalid input. Please enter a valid number.")

