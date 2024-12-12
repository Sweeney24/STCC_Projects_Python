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

def getMedian(user_list): #function to find median
    user_list.sort()#bringing in the value input into the function and sorting it, lower value to highest
    if len(user_list) % 2 == 0:#determining if the list length is even with modulo
        #the below code uses the builtin int() and len() functions to make accessing the index viable.
        middle1 = user_list[int(len(user_list) / 2) - 1] #variable for the middle number, by accessing the index in the middle of the list, minus 1.
        middle2 = user_list[int(len(user_list) / 2)] #variable for the next middle number, again by accessing the index.
        median = (middle1 + middle2) / 2 #simple math using the stored variables to find median.
    else:
        median = user_list[int(len(user_list) / 2)] #simply assigning median here by accessing the index at the middle with simple math.
    return median

def main():
    uRealEstateValues = [] #empty list to be populated by loops below
    while True: #continues looping until not true, or it reaches the builtin break.
        uSalesPrice = getFloatInput("Enter in the sales value:")
        uRealEstateValues.append(uSalesPrice) #using builtin .append() function to append to the list in this function.
        uAnotherValue = input("Enter another value yes or no: ")
        # loop to evaluate user input to see if it DOES NOT match the tuple and uses the builtin function to automatically make the input lower case
        while uAnotherValue.lower() not in ("y", "yes", "n", "no"):
            uAnotherValue = input("invalid entry, enter (y)es or (n)o")
        if uAnotherValue.lower() == "n":
            break #breaks this lower loop, returns to the upper loop of getting another sales price


    uRealEstateValues.sort() #use the builtin function to sort the list
    uPropertyNumber = 0 #declare this variable so it's value can increase through each iteration of the for loop below
    for saledata in uRealEstateValues:
        uPropertyNumber += 1 #increase value of variable
        print(f'Property {uPropertyNumber}: ${saledata}') #print out the individual value of each property entered
    print(f'Minimum: ${uRealEstateValues[0]}') #print out the minimum by accessing the first index
    print(f'Maximum ${uRealEstateValues[-1]}') #print out the maximum by accessing the last index
    print(f'Total: ${sum(uRealEstateValues)}') #print the sum using the builtin func
    print(f'Average: ${sum(uRealEstateValues) / len(uRealEstateValues)}') #print the average using builtin and simple math
    print(f'Median: ${getMedian(uRealEstateValues)}') #print median using the function specific to this class
    print(f'Commission: ${sum(uRealEstateValues) * .03}') #print the commission by using builtin and simple math

main()
