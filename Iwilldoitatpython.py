from random import randint
from math import e
from statistics import mean
from time import sleep

# Random coment
class AI:

	class weight:
		def __init__(self, input, precission):

			self.inputslist = input
			self.weights = []
			self.precission = precission
			self.result = 0
			self.parameter = randint(-10,10)

			for i in range(len(self.inputslist)):
				
				self.weights.append(round(randint(-10,10),self.precission))

		def resultFunction(self):

			self.result = 0

			for i in range(len(self.inputslist)):
				self.result =self.result + self.weights[i]*self.inputslist[i]	   
			self.result = self.result + self.parameter

		def resultAI(self):

			AIprediction = []

			self.resultFunction()

			#Activation Function Sigmoid

			Sigmoid = round(1/(1+e**-self.result),self.precission)

			AIprediction.append(Sigmoid)

			return AIprediction

		def errorFunction(self, realResult, predictedResults,mistake):

			# the error is now calcultated 
		 
			costFunction = -2*(realResult - predictedResults)*(round(1/(1+e**-realResult),self.precission))*mistake

			Xgradientlist = []

			for weight in self.weights:

				Xgradientlist.append(costFunction)

			Ygradient = costFunction * self.parameter
			# Now corrects the function to a new one 
			  
			print(self.parameter - Ygradient)
			self.parameter = self.parameter - Ygradient

			newWeightss = []

			for newWeight in range(len(self.weights)):

				 

				newWeightss.append(self.weights[newWeight]  -  Xgradientlist[newWeight])
				 
			self.weights =newWeightss 
			self.parameter = Ygradient

			self.resultFunction()
			 
x = AI.weight([-0.5],5)
x.resultFunction()
x.resultAI()

for i in range(1000):	
	x.errorFunction(1,x.result,0.01)

print(x.resultAI())
print("\n" + str(x.weights))