import math 

def CalculateE(roundVal):

		someE = round(math.e,roundVal)
		return someE

roundTo = input('Enter the number of digits you want after the decimal for e: ')
try:
	roundint = int(roundTo)
	print(CalculateE(roundint))
except:
	print("You did not enter an integer")