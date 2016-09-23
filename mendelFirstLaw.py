from __future__ import division #Python3 division yields floats from integer division
alleleDistribution = "19 30 24" #Composed of "k m n"

def Main():
	genotypeList = convertListToGenotype(getIntList()) #Working up to here
	print iteratePossible(genotypeList)
	
#Converts the allele distribution into a list
def getIntList():
	list = alleleDistribution.split()
	for i in range(len(list)):
		list[i] = int(list[i])
	return list

#Convert k m n to k*AA m*Aa n*aa
#2 2 2 = AA AA Aa Aa aa aa
def convertListToGenotype(numList):
	gl = []
	d = ("AA "*numList[0]).split() #Dominant
	h = ("Aa "*numList[1]).split() #Heterozygous
	r = ("aa "*numList[2]).split() #Recessive
	gl.extend(d)
	gl.extend(h)
	gl.extend(r) #Add all three together into gl
	return gl
	
def iteratePossible(gl):
	numPossible = 0
	numDominant = 0
	for P1 in range(len(gl)-1):
		for P2 in range(P1+1, len(gl)):
			numPossible += 4 #4 resulting genotypes from each cross
			numDominant += combination(gl, P1, P2)
	return numDominant / numPossible

def combination(gl, P1, P2):
	if (gl[P1] == "AA" or gl[P2] == "AA"):
		return 4
	elif (gl[P1] == "Aa" and gl[P2] == "Aa"):
		return 3
	elif (gl[P1] == "Aa" and gl[P2] == "aa" or gl[P1] == "aa" and gl[P2] == "Aa"):
		return 2
	else:
		return 0
	

#Entry of the program
if __name__ == "__main__":
	Main()