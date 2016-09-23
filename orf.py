input = ''.join(""">Rosalind_9851
TCCAGTAATGGTGGTGCGAGATCTACTGAAGGATCCACTCAGGTTCTTGGTGGTGCGATC
TATCGAGGATACAGTGCTAGTGTCCCGCAACACGTCCACTCCTGGATTCGGAGACATGAC
ACTTAACTAAGCTCTCTTCACCCACCCTCGCCGGCCGGGGCCTCGAGAAAAAGTGGATTA
CCCCGAATGTAGACATGGTTTAAGGTTCCGACTCCCTCTGGACTATAAACGCCGCATAGC
GATAACAGTCACTAGTCGCGGGACTTCCCCATAGACCTGTCAACGCCCAGGAAGAGGCGC
CCATCTTAGTACTTCCCATCATCCGCCAGGTTCTCGACTAGGACCTACATTTCCCGTCGG
TCACCAGCCTGTCATCTGGTTGGAGCCATGACTTCAGTGGGTAATGCTGTGTTACTATTA
GGAAGGATTTAGAGAAGCGATTTTATCTGTAATGGGACCGCCATTGTAGAGTTTGCGGCC
CCTCTAGCTAGAGGGGCCGCAAACTCTACAATGGCGGTCCCATCCGCGGCCACGCCGTCA
CTACCCAGCGATCCAATTATTAAATTGGGCGAATAGAGAGCTTAGTCGCACCGGGTCTGG
GCGGGGCGCGCTGTATTAGATTGCAGAGCCGTCCCCGTCAACCCATGTTCGGGCAACGAG
TCGCTACAGACAAATTGAGGATGCAGAGGCCTGCTGAAGAGCGCAAACTCTTGAGCCTAA
GAGGACAAACGAATCAAAAATACCTACATCTGGGACTTTTCTTCCACATCACGTCTTCCC
CCCTATGTACAAGCTGGACCTCCGTTGCTTCCCTCATTCGCTAACGCTCGCTTCCTACAA
TGCCTTCATTGCGCGCTCACTTTCCTGCGTACACGGACTGTCCCTACTGAGAACATGATG
ACAAAGCTTGGGCTTGGAGGGACTCCACGGTCGACACTGTAGCTGTCTACCCTTTGGATG
AGCAGTATCGCAAA
""".split()[1::]) #Input dna string

codonTable = {  "UUU":"F","CUU":"L","AUU":"I","GUU":"V",
				"UUC":"F","CUC":"L","AUC":"I","GUC":"V",
				"UUA":"L","CUA":"L","AUA":"I","GUA":"V",
				"UUG":"L","CUG":"L","AUG":"M","GUG":"V",
				"UCU":"S","CCU":"P","ACU":"T","GCU":"A",
				"UCC":"S","CCC":"P","ACC":"T","GCC":"A",
				"UCA":"S","CCA":"P","ACA":"T","GCA":"A",
				"UCG":"S","CCG":"P","ACG":"T","GCG":"A",
				"UAU":"Y","CAU":"H","AAU":"N","GAU":"D",
				"UAC":"Y","CAC":"H","AAC":"N","GAC":"D",
				"UAA":"*","CAA":"Q","AAA":"K","GAA":"E",
				"UAG":"*","CAG":"Q","AAG":"K","GAG":"E",
				"UGU":"C","CGU":"R","AGU":"S","GGU":"G",
				"UGC":"C","CGC":"R","AGC":"S","GGC":"G",
				"UGA":"*","CGA":"R","AGA":"R","GGA":"G",
				"UGG":"W","CGG":"R","AGG":"R","GGG":"G"} #STOP has been replaced by an asterisk (*)

def convertToRNA(s):
	proteinString = ""
	string = ""
	i = 0
	for i in range(len(s)):
		if s[i] in ['A', 'G', 'C']:
			string += s[i]
		elif s[i] == 'T':
			string += 'U'
		if len(string) == 3:
			proteinString += codonTable[string]
			string = ""
	return proteinString

def complement(s):
	compDict = {'A':'T','T':'A','G':'C','C':'G'}
	return ''.join([compDict[s[i]] for i in range(len(s))])
	
inputPerm = [input, input[1::], input[2::], complement(input[::-1]), complement(input[-2::-1]), complement(input[-3::-1])] #All possible permutations of an input string
inputPerm = [convertToRNA(t) for t in inputPerm]
#All possible permutations are now generated - now we need to search for M[...]* and print M[...] from that

orf = {}

for i in inputPerm:
	try:
		for j in range(len(i)-2):
			if i[j] == 'M':
				stop = i.index('*', j)
				orf[i[j:stop]] = 0
	except ValueError:
		continue
		
for i in orf:
	print i