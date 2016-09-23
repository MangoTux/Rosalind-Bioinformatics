input = "19198 17354 16006 18160 19079 16731" #6 integers -> AA-AA AA-Aa AA-aa Aa-Aa Aa-aa aa-aa

ratio = [1,1,1,.75,.5,0] #Ratio of dominant phenotype to total

def Main():
	list = convertInputToGenotype()
	total = 0.0
	for i in range(len(list)):
		total += 2*list[i]*ratio[i]
	print total

def convertInputToGenotype():
	list = input.split()
	for i in range(len(list)):
		list[i] = int(list[i])
	return list
	
if __name__ == "__main__":
	Main()