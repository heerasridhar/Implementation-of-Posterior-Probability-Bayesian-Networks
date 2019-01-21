class BayesianNetwork(object):
	def computeProbability(self, b, e, a, j, m):
		result = (self.givenProbability("B",b,None,None) * self.givenProbability("E",e,None,None) * self.givenProbability("A|B,E",a,b,e) * self.givenProbability("J|A",j,a,None) * self.givenProbability("M|A",m,a,None))
		return result

	def givenProbability(self,query,value1,value2,value3):
		if query == "B":
			if value1:
				return 0.001
			else:
				return 0.999

		if query == "E":
			if value1:
				return 0.002
			else:
				return 0.998

		if query == "A|B,E":
			if value2 and value3:
				temp = 0.95
			if value2 and not value3:
				temp = 0.94
			if not value2 and value3:
				temp = 0.29
			if not value2 and not value3:
				temp = 0.001
			if value1:
				return temp
			else:
				return (1-temp)

		if query == "J|A":
			if value2:
				temp = 0.9
			else:
				temp = 0.05
			if value1:
				return temp
			else:
				return (1-temp)

		if query == "M|A":
			if value2:
				temp = 0.7
			else:
				temp = 0.01
			if value1:
				return temp
			else:
				return (1-temp)

	def calculate(self,variables):
		if not None in variables:
			return self.computeProbability(variables[0],variables[1],variables[2],variables[3],variables[4])
		else:
			index1 = variables.index(None)
			new_variables = list(variables)
			new_variables[index1] = True
			val1 = self.calculate(new_variables)
			new_variables[index1] = False
			val2 = self.calculate(new_variables)
			return val1 + val2

	def generateValues(self,variables):
		result = []
		if "Bt"	in variables:
			result.append(True)
		elif "Bf" in variables:
			result.append(False)
		else:
			result.append(None)

		if "Et"	in variables:
			result.append(True)
		elif "Ef" in variables:
			result.append(False)
		else:
			result.append(None)

		if "At"	in variables:
			result.append(True)
		elif "Af" in variables:
			result.append(False)
		else:
			result.append(None)

		if "Jt"	in variables:
			result.append(True)
		elif "Jf" in variables:
			result.append(False)
		else:
			result.append(None)

		if "Mt"	in variables:
			result.append(True)
		elif "Mf" in variables:
			result.append(False)
		else:
			result.append(None)
		return result


from sys import argv

given = False
observations = []
query = []
for i in range(1,len(argv)):
	if argv[i] == "given":
		given = True
		continue
	query.append(argv[i])
	if given:
		observations.append(argv[i])

bnet = BayesianNetwork()


if query:
	numerator = bnet.calculate(bnet.generateValues(query))
	if observations:
		denominator = bnet.calculate(bnet.generateValues(observations))
	else:
		denominator = 1

	print "The probability is : %.9f" % (numerator/denominator)
else:
	print "Invalid string"