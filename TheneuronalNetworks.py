from random import randint
from math import e
from statistics import mean
from time import sleep


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

			for i in range(len(self.inputslist)):self.result =self.result + self.weights[i]*self.inputslist[i]

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
		 
			costFunction = 2*(realResult - predictedResults)*(1/(1+e**-realResult))*mistake

			Xgradientlist = []

			for weight in self.weights:

				Xgradientlist.append(costFunction)

			Ygradient = costFunction
			# Now corrects the function to a new one 
			  
		 
			self.parameter = self.parameter - costFunction

			newWeightss = []

			for newWeight in range(len(self.weights)):

				 

				newWeightss.append(self.weights[newWeight]  -  Xgradientlist[newWeight])
				 
			self.weights =newWeightss 
			

			self.resultFunction()
			 
x = AI.weight([0],5)
 
n3 = AI.weight([0],5)
n11 = AI.weight([x.result,n3.result],5)
n12 = AI.weight([x.result,n3.result],5)
n111 = AI.weight([n11.result,n12.result],5)
x.resultFunction()
x.resultAI()


# Here put the result you want
result = 1 
print(round(3.122121,3))
while n111.resultAI()[0]<result-0.1:

	try:
		for i in range(1000):	
			x.errorFunction(result,x.result,0.01)
			n11.errorFunction(result,n11.result,0.01)
			n111.errorFunction(result,n11.result,0.01)
			n12.errorFunction(result,n11.result,0.01)
			 
			n3.errorFunction(result,n3.result,0.1)
	except Exception as e:
		pass
	 
	


print(n111.resultAI())
print("\n" + str(n111.weights))