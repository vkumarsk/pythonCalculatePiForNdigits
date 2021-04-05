import math

def CalculatePi(roundint):

		somepi = round(math.pi,roundint)
		pi = str(somepi)
		someList = list(pi)
		return somepi
roundTo = input('Enter the number of digits you want after the decimal for Pi: ')
try:
	roundint = int(roundTo)
	"Us of Decorator function"
	print(CalculatePi(roundint))
except:
	print("You did not enter an integer")