#This quick program will calculate your weight on different celestial bodies.
#For Prof. Candido's python programming class.

#Named Constants. These never change. Not unless there is some interplanetary catastrophe.
nMERCURY = 0.38
nVENUS = 0.91
nMOON = 0.165
nMARS = 0.38 #funny that the surface gravity factor is the same as Mercury.
nJUPITER = 2.34
nSATURN = 0.93
nURANUS = 0.92 #renamed in the year 3001 to Urectum (thanks Futurama)
nNEPTUNE = 1.12
nPLUTO = 0.066 #no longer a planet

print("We're going to calculate how much you weigh on other planets!")
uWeight = float(input('Please enter your weight in pounds. ')) #converts the user input string to a float

print('Awesome, below is a table of your weight on other planets.')

#simple arithmatic to get the weight on the target planet
mercWeight = uWeight * nMERCURY
venWeight = uWeight * nVENUS
lunaWeight = uWeight * nMOON
marsWeight = uWeight * nMARS
jupWeight = uWeight * nJUPITER
satWeight = uWeight * nSATURN
urWeight = uWeight * nURANUS
nepWeight = uWeight * nNEPTUNE
pluWeight = uWeight * nPLUTO

#there must be a simpler way to make sure the colons are aligned.
print( '{:10}'.format("Your weight on Mercury  :"),  format(mercWeight,"15,.2f"))
print( '{:10}'.format("Your weight on Venus    :"),  format(venWeight,"15,.2f"))
print( '{:10}'.format("Your weight on the moon :"),  format(lunaWeight,"15,.2f"))
print( '{:10}'.format("Your weight on Mars     :"),  format(marsWeight,"15,.2f"))
print( '{:10}'.format("Your weight on Jupiter  :"),  format(jupWeight,"15,.2f"))
print( '{:10}'.format("Your weight on Saturn   :"),  format(satWeight,"15,.2f"))
print( '{:10}'.format("Your weight on Uranus   :"),  format(urWeight,"15,.2f"))
print( '{:10}'.format("Your weight on Neptune  :"),  format(nepWeight,"15,.2f"))
print( '{:10}'.format("Your weight on Pluto    :"),  format(pluWeight,"15,.2f"))
