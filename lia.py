input = "2 1" # k (k<=7), N (N<=2**k)
#Polynomial works here, too!

class BinaryTree():
	def __init__(self, rootid):
		self.left = None
		self.right = None
		self.parent = None
		self.rootid = rootid #Value of rootid is 2d array -> Probabilities of ([AA, Aa, aa], [BB, Bb, bb])
	
	def getLeftChild(self):
		return self.left
	def getRightChild(self):
		return self.right
	def getParent(self):
		return self.parent
	def setNodeValue(self, value):
		self.rootid = value
	def getNodeValue(self):
		return self.rootid
	def getProbability(self):
		return (self.rootid[0][1] * self.rootid[1][1])
		
	def insertRight(self, newNode):
		self.right = BinaryTree(newNode)
		self.right.parent = self
	
	def insertLeft(self,newNode):
		self.left = BinaryTree(newNode)
		self.left.parent = self

def Main():
	numGenerations = int(input.split()[0]) #Get the number of generations to iterate
	offspringThresh = int(input.split()[1]) #The threshold for probability at least offspringThresh of generation numGenerations is of genotype AaBb
	numOffspring = 2**numGenerations
	tree = BinaryTree([[0, 1, 0], [0, 1, 0]]) #Create the first generation of genotype AaBb
	#print tree.getProbability() #Working up to here
	tree = populateTree(tree, numGenerations)
	#Get sum of probabilities of AaBb at level numGenerations, divide by offspringThresh

#Fill the tree with appropriate values for all of these - Check if this works
def populateTree(tree, numGenerations):
	tree.left = BinaryTree(calculateOffspring(tree.getNodeValue))
	if (numGenerations > 0):
		populateTree(tree.left, numGenerations-1)
	tree.right = BinaryTree(calculateOffspring(tree.getNodeValue))
	if (numGenerations > 0):
		populateTree(tree.right, numGenerations-1)
	return tree
	
def calculateOffspring(gl): #[AA, Aa, aa], [BB, Bb, bb], independent
	for i in range(2):
		for j in range(3):
			gl[i][j] = .25*gl[i][j] #Algorithm is wrong - Fix
	return gl
if __name__ == "__main__":
	Main()