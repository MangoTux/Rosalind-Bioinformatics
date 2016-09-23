#Computing GC Frequency
from __future__ import division
#Input phrase containing <= 10 DNA strings in FASTA format
input = """
>Rosalind_6379
ACCGCGGCAAACGAAGTTTTTCGTACGGTTCGAGTCTCCAACCGCGCAAATAAAGCAGCACTATTTACCGGGTTCGACCTGAGCTGGTTCCTTGGTTTTATACGGTCTGAAGCTATTTGGACCCCGGAGAAACAACAACCGCTGACCACGACTCGACAGATTGTAAGGCGCGGACCATTTTTAATCGGGCCGTAACTCTGAGGACGATCCTCGGTTTATGTCAAGATCGCTCAACGAATCGCGTAAGCTTTAAGCAGATGGAAGCAGCCTCTTACCCAACTCCTCATCAGTGAGAGTTCTAATCGCGCATTGAATGTGAGAATCGTTTACTGGGACAGCAGGCGCCCCTCTGGAGTCTTTCATGCCAAATACGATTCCACCGAGACAAAGGATGCATGGCTAGGAGTGGTGTTATATTTGTACACTGGCAATCTCAGGGCCATGCTGTGGGGTGAGATTTAGCGTCGCAACTGTCATTTTACTACACAGAGTCTAACTCCATGACAGGCATGACCCGTTAGTCACGTCCTTCAGGTCGCGTCGAGTATGGCGAGCCATCAGTGCTGCGTGACCGACCCAACGATCGCAGTGATGCTAGGCCCGTTTTAAGCCAGTTTGGAAAACTAGTCCTTATACGTGGAGTACAGTCACGACCCAGTTATCTCTTGTCGTGTGTGGAGGCATGCGAAACACTGACGCTTATTGCTTTCGGGTGGTCACGGAGGGTTCGCCAGCCGGGGGACGTACGGAGTCGAAAGATTGGACTGTGGAGAGAGTAGGGCGTCCCCTCACTACCTAGGTCAGTAGGAACTGGCGGACACCAAAGTGACGTGGCTCATTATGACCATCACACCGCTCTATGTGCGGACACTAGTTTAGCGGTAAAAGAGGTCGTCG
>Rosalind_6124
GTTACGGACGCAAGTACCTGAGTTGTTCTTACCAGTGTTCTTCTGCACCTACTGGAAACCATTATGAAGTTCGCTTGAGTAAGTATCTCAAGCATTGGGGGCGAGGCCGCATTGCCGGAGGCCGAGATGTGACCCGTTAATGAGCGTAGTGTCCCTGGATAGCGTCTGACGCCGAAATCATCATGGTATGGACCGCCCCCTGAAATACCTTCATGGTATGCGACTGCCAGTAACGCGTCAAGTAAGCCCCCTGACCGCCAGCGTCGGCATGAGCGGACTTAGTATGAGGGAACTATCGCGCTCGAGCAGACGCCAGATGTGGACCTAGTCCAACTAGTATAGTGATTCAGGCTTTGACCGCGCTAGCTCGAAAAAAAGAGCAATCTCGCAAGAGGGGTTAAAGAAGTATAAGAATCGATGAAGTCCCACAGTAACTGAGGTGGTACACTTGCGTGAACCTTGAAACGTACTCAAGCTGCAACAAAACAGTTGGATCATGTATAGGTCCTCACGGCCCGTGGTGCACGGCCCGTAGCTCAATGAGATAGTCCCGCGCAGTGACAAGTCCATGAAGTGAGGTTAAGATGGGCTCTGGTACAACAAACAAACGCAGCAGCTAACACAAGAGATAGGGGAGATGTAAGTGGCATTTCGGTTTTTCTGGCTCGACACAGCATGACTTAAGAGTTTGTCAAATTGTTTGACAAACGCAATCTAGGCTAATCCAGAATTCCTAGAACTTACGGGTGCGAAGCCGTGACACACGTCCGTTTGGGAACTGAAAGTGTGTTAACCCATCAGCTCAACTGCGTACTCCCGCTCTAATAGATTCACCTCATATCGACAAAGTTGGACTGTCAGCACAAAGTGCTTGAATTAACAGTGGTTAACGGGTTATGTCGATTAATACCATGCCGCGCACCATAACCCGCGCCCCTCAATCTGTTTCAGATTAAAAAGCAGACTCTCAAAATGAAATGAAAC
>Rosalind_4428
CGCACTGGAGGTCATGCGCGGGAAGGTCGTCACGGGTGATCTTGTCATAACTAAGGGTATATCGTTTATCTGAGCTGCTACCCAAAGTTTCAGGGATCGCATACGCGAGAGACCTGGTTGGCTAGACCGGGCAGCTAACAAGCGAAACTGATGGTAATAATGCGTAGAAACCAAATACCCGCTATTCCTCGTTAATACCGCTTACGGCCGTATTGCGTAAGACCGGTGTTTTACGTCGGCAGCGCGACGCTCTAAGGTACCAATCGTAGCGGTGTTCCCAGGATGCCTCCGATGTGGATAACAAGCATAGATTCGCCGGATCGTGAAGGTTGTGGCTTGCTCATGTCTAACGGAGATTTCGTGAAAATGACAAGGTAGCCAGGCGAGGTGTGTGAGCAAAACTTAGAACCACTCCCTCCAAGCTAGAGCAACAACCCTGTCAGGAAGAAGGATCGAAGGCGGTATACATTGCAAAATCTATCTGGCCCTTCGGCATTAAGTTGTCCGGCTGGCCGACGTGTACAGGGCAGTACGACGTAATGGCTCAGCACGGCACCGTTTTGCAAGTCGCCAGCCGGGCGGCTCAGCGTAAGTAAGTAAACATAAGACACCAGCGATTACCCCCCTTTAGCCTTGTTGCTCTCTGGCATAGTCCCTATCCCTCGATGTGCGCCGAGCAGTCTTACCTATGGCCTCGTTACTCTCACTGTCCAACTTGGAGCTGCATCTTCTTCCCAGTTGTCTCAGTTCATCCTCACATAACCATCCCACTGATCCTTGTTCCAGCGTTCTAAAAAACGGAAGTAGGACAAGCCTTATGAGGTTGCGAGTCATGTTTAACCCCGCATATGTCTACGATAGGAGAGACAAAGGAGGCGCCGATCCTCAATCGGCAAATGCTGATTTCAATTGATACTCTGGCCGGGGGTGAAATGGAGCTTACAAAACTTTATAATGGTGGA
>Rosalind_3395
ACGAGCACCGAACGCCTTAATCTTCAAACCCCAACTGCTGTCTCTGTCCGTACACAGCGTACCCCTCGACAGCAATTCCCGGTCCACTCCCCATAATTCCCTGGCATAAAGGAGTTGCAGGCCATAAGACAAGGGACATCCACAAAATGGAGCATACGACTGCCGTAATCGTTTCACCCGCGCTTAACCGCGCACTAGTTAGATGTCTCGGGCCGTTAGTATCGACTTCTTTGGGATAGCAAGACATGCTCTGCGTACGAAGTAGATCGTTGTGCGGGACCCCCCCATGCCGTCCTGCAACCGTGGGTCCTGAAACGGTTTGCGGTAAAAATGAACGCGCTAGAGATAAGTCAGACTCACAGTCTTCAGGCAACGCCTCCGCCATGTTAAACAAAGCTCCTGGCCTTCCGGCGACTGGGAATCTCACGGAGTTCTATGGCTCGTAACTAAGGGCGGAAATTGGAAGGATAAACGGACTGATCTGAGTTGTCGCAGCTAAGAACATCGGTCGGCCCTGTTTGATCAATTATAGACACTGACGGTATATGACTGAACTGGTGTTGCGTCGTGCTTTGGTCGCGCGACATCTTCTGGCCTCAAAACTACCCGGTCAGGGGATCCCGTGTTTCAAAGACGCTAACGGTCACATGAAACTCAACGCAGGTGTTGGTTCGGCACGGGCGGCTGATGCCTTTACACCTTTCCGCGTGCATCTTTAATGTTACTGGCCAAGCTTCTGTAGTTCCCTCCGCGCATCATATACAACGGGATTGGATTCTGAATGCAGTGCGTGAGTCGTGGACCAGGGATAAACATACATCAATACGTTTACAGCGATAGCGCGGTGCTGGTTGCCATTTGCTGCGAGTAGGGCGAGTTACGCCGGTCGGCATATGGCTGCGCTCGTGGCTGTCCTAGTCAGAACAATTAGATTTAGGTGGAAGAACCTTAGCTGGTACCCAATTTTC
>Rosalind_5009
CAAGACAACAGGACATACCATAGCGTTGACCGTTAATTAGAGTGCGGATTCAATACTGGGTATACGTGAATAGAATTCGACTCCTCTTCGGTCAGACGTGGGCCGGGGATAGTTAAAGGTTTGGCGCTACGTAGGGGGACTCTCAAGCTGCAGTCAACTCGGGGCCCGTCGAAGTGGAGACATAACGCGTAGGATCAACAGGCCCGGTTGTGGAGGTCATAAGGATTTCTCACCGTGTCGAAGTTCGTGACCCGTGAAAGCCGGCGTTTGGTGCAAAAATATATCTAATTCGCTTCCATTTTGTTTGTAGGCGATACCCGGTTGCAAAGAGTGTGGTAGTCAAAGCCCAAGCCTCCCGGGGGATATTGGCCTAGTTTGCGTCCGTGCTGTCGGTTAAAATACCGCTGGTTTTCTCACTCTGCCCTTATAGAAAACGATTGTGGCGAATGGATTCCATTTTGTGAGATTATCTTATTACCCACTTTGTGAATCTGGTGCTGTTCTTGCACTGCCGAGTGCTGTGTCTACTGAGCCGTACGGGAAGGTATATGAATAGAAATGTCCTGGCACCTCCACGGGTGTAGTACCACTCGTGTCCACTAGGGATTAGACAATGATAAAATTCTGATTTGTAAGGAGCGTCGGTCTGATAGGGGCATGGACCTCCATATAATATCTCGGCGGAAGATAAGCAGAATACTTTATGCCTGGGGGTCTAAACTCCACCCCCCAAAGACAAGCGGAAATTCTCCCCTCTAATCTCCCTGTAATCGGGTGTGAGGACAAGACGCGGGTCCGACGTTGAAGACAGCCCTTTCTAGCGTTTCATCAGGAAGTTTACTCGCACTTTAACCCACTAAAAATATCGGACCATTCTCGGCGAAACGGTCCAGCATTAATGGAA
>Rosalind_7448
GCAGGCGCTGCCATAGACAATCGTATGTAAATGAATCTTGGCAAGATCGCGTGGAATGCCTGTAGACCTACGAGGATTTCTACCTAGGCCTGCTGGCGGGATTGGGTGTCGTTCGTTTCGCCGAAGGACCTACTGTTAACTAGGAGAACAATCTTTGCCAGAATAGAGTCGTTGTCCCAATGTAATTTCGTAGGTTTGCCACGGACTGACAGAGTACTAGTGTCGCCCGCATCCGGGCCATGTGTCGTCTCCTCTGAAGCCATCTTACCGAGAATTGGCTCCTGAGTTACCACCGCCCCGGGAATTACCTATCCCGTTTCGCAGTGTTCTGACCTCATAAACGTGGTCGCTCTAATTGTCTGATTAATGGCCGCATCGCAAGAGCGGTGTCATTACCAGCGGTTATAGGATGACGGTTCGTTGCTGGAACTGATGACCTATGTCCAGATGCAGCCCCTTAGTTTTACCCCGTAAGGGATTGTACTTACACTGCGATCTTAACTAAGACGCCTTCCGGCTAAACGCTAGACAGGTGGGTCGGATGGTCTCAGTTAGCCCACGATTGATAATTGGATGCTTCCGTTTGAAAGTCTGTTTGCCGCTGACGCGCAAAGGGCGCGAGCCGCTGGGCGTGACTACACTACTGAAGATGAACCGCAACCCGAGCACGCCGGATCGCACTACGTAAACTGACCGAGGCCTTTCACTTATGCGATCCAATAATCTTAAGGGCAGCTATACATTTAGGACCATATAGTGCTATTTTACTTTCACTCAACGAGCAGTAAGATCGAGGGACGCTATGTGTTTCGATGACTCACGCCCCACAGTCTACGCGGGATCCACTATGGGCCATCC
>Rosalind_5649
TCTGCATGGGTGTACAATGAATGAAATACCAGCAATGCCTCTGCAGCATGAAGACAGATAGGAGCAGTTCGCCTGGCGATAACGTGCTAGCCGCTCGATGTTTCGCCCTGCACTGGCTTAATCCTGCTTCTAAAATCCTTGATCATCTGCTGACTACTAACGAGCCTACGTGATCGGGTCATATCGTACACAAGGAGCATTGTATAGTGAGGGCCGTCGAGGAAAAGGCTAACCTGTCTGAACATTCTAAGCCGGGCGGCTCCTATGACCTCTGCAAGTGCCCCGCGGGCTAACTTTATAAAAACTTATTTCTATCGTTTCCTCGCAGTGCTGGAGAGGATCATGCTGACAAAACACTGCCACAACGCGTGGGAGCTAGAACTGGCTCCACACACTGTCCTTTCCCTGACTACTGACCCATCAGACTGGCTACCCCGAGCATTGGCGCCCTCGGGCCAATAATTAAAGAGCCGCGCCATAAGGTTCAGAAGGGAAACTCCGGGTCCGTCTTGCGCTTTGGAGAATCCCAGGGAAGAATTCAAGGTACAAATGCGAAGGTAGCTGTGCGAGGTAGTCGTATTCTCTCGCGCGTACAGCCATTAGTAAAGACATTCGTTTCTGGGCTCGGAATGCTGGGCCTTAGCGACGCTCCAGCCTTGTCAATAAACTAGGTGCCTCCACTTCACTAGATTATCGAAGAAGATTGCGGCTTCTGTGAATATATCGCAAACCAAGTCCGAAGGCCCAGGATACCCATAATCAGACGGGCCAGACAAGGTTAAAACTAATAATCACCGAGGGCGAACATAATTTGCGCGACCTACTGCTATTGCGGCACACGCTACCTCGCCCAAGCCCTACCACACA
>Rosalind_5127
GACGGACGCTCGTGCGCATGGATGGACGGTGATTGATTCGTGATGGCTGTGAGCGGTAAATACATAAATGAACCTCAGATCCTTCATTCGCAATACACTCTCTCGCTTAAGGAGGTGGGTTGATGTCAAGTTTTGCTATGGCATTGACTACAGAAGGTAGGGCAGCGGGTAAAAGTCGAATCAGACAAGTGACCGGGCAACTTTGCATCGATCCTCGTTTAATGCCACTAGCACGTCTAAGCACTGTTCAGTCTCTACCCCACGTCGCGCAAATCCCCTATGATTAGTGTTTATACGCATTTTTGCTCACCCGTACGCGGGGTCAGTTTGCCTGGCGTTGATGCCCCCTTCTGGTAATAGAACGGGAGCGTTCGATAGGCCAACCAAAAGCCCAGCGTTTCCGGCAAGTTGAGAACAAGGTACTATCCAGCATCCAATTTTACAACGTATACAGTGAATGGAGTAGTCGGTATACATCCTACCACGACAACACCTACGTTACGGGTACTCCAGCTCGCTCGAATGTAGCGTGGCGAACCCTTCCGTGAATATGACCGCAATGACTACTTATCAGAAGGTCTGACCCAGCGCTCTCATCCTTGGATTATGTCGCCGATCTTATACTAGAGGTATGAGTCACCCCATAGCCTTTTCCACCCGTGCGACCACCGACGTGCCACATATGCTACAAGCAAGCCTTATGATCACCCTGTGATTGTTCGGTCTCTCTCTTATACTCCGCCTCTACCACGCAAAATTATACTACAGTGGATCATAGGTGGGGGAGGTCATACGAGCAAAGCT
"""

class FastaCode(object):
	def __init__(self):
		self.name = ">Rosalind_0000"
		self.sequence = "CATGAG"
	
	def __init__(self, name, sequence):
		self.name = name
		self.sequence = sequence
		
	def getName(self):
		return self.name
	def getSequence(self):
		return self.sequence
		
	def setName(self, name):
		self.name = name
	def setSequence(self, sequence):
		self.sequence = sequence

def getGCFrequency(string):
	num = 0
	for i in range(len(string)):
		if string[i] in ['G', 'C']:
			num+=1
	return num/len(string)
	
def Main():
	dnaStrings = input.split()
	print dnaStrings
	fastaList = []
	for i in range(0, len(dnaStrings), 2):
		fSet = FastaCode(dnaStrings[i][1:], dnaStrings[i+1]) 
		fastaList.append(fSet)
		
	maxGC = 0
	name = ""
	
	for i in range(len(fastaList)):
		gc = getGCFrequency(fastaList[i].getSequence())
		if gc > maxGC:
			maxGC = gc
			name = fastaList[i].getName()
	print name
	print maxGC*100
	
if __name__ == "__main__":
	Main()