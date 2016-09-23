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
				"UGG":"W","CGG":"R","AGG":"R","GGG":"G"}

def Main():
	input = "AUGGUCUACAUAGCUGACAAACAGCACGUAGCAUCUCGAGAGGCAUAUGGUCACAUGUUCAAAGUUUGCGCCUAG"
	proteinString = ""
	string = ""
	i = 0
	for i in range(len(input)):
		if input[i] in ['A', 'U', 'G', 'C']:
			string += input[i]
		if len(string) == 3:
			proteinString += codonTable[string]
			string = ""
	print proteinString
		
if __name__ == "__main__":
	Main()
	