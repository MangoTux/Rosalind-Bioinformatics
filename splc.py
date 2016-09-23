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
				"UAA":"Stop","CAA":"Q","AAA":"K","GAA":"E",
				"UAG":"Stop","CAG":"Q","AAG":"K","GAG":"E",
				"UGU":"C","CGU":"R","AGU":"S","GGU":"G",
				"UGC":"C","CGC":"R","AGC":"S","GGC":"G",
				"UGA":"Stop","CGA":"R","AGA":"R","GGA":"G",
				"UGG":"W","CGG":"R","AGG":"R","GGG":"G"}

input = """
>Rosalind_8567
ATGGGTAGTCACCGATATACCAAACAGGTGGACGAACCGCAATTTCACTTTGTTCTTTCTCACCGACAGGCCCAAGGGCTTGAAGGATGCGGCAGACAAATGCACGCGTATATCACTACCGGTGCCGGTAGAGCGTGTAGTTTGATTGTCCGGGACCGCGTTGGCAGAGCCTCATCTTTCCCGATGCCGCCGTCGAACCCAGTCTCGGTTGATCCGTCCCATCACGAAATGAAAACAATCTATCCCATCATCCTATCGGACGGCGTGCATGCCGGCTAAGCAGCCTGAAATTAAACCGCCTTAAAGTCACCCCTACCCTCAGGTCTTGATTGCGCTTTCACAGGTTACCGTATGGAGCGACATTCAATAGCAGATCGTCTGAAAACCCGAGTCAGCAATTACGGCAAGTCGCACTGCGATTTCTGCGTGAGCCAGACAACTTACCATAACTGGTCAGCCGCCTGCCGAAGACGAGGCCATTCTTCCATCAAGAACCTCGGACCCAGGACCGGCCTGGGGGGCTTGGTGAAAGCCTAGAATTTGTTGTATTGACGGTACGACTTGTATTCGCCTGGATACCAATTACATCTTATGTATTATCATCTACATAGACAGTACAGAATCGGGCCCAGAATGTCATTGGCATTCTTAATTGACGCGCATGTATGTTTGGACATCTATATTCCGTCACAATTTACGCCTGGGTGTACCAGTCGTTCCAGTCATGCTCTACACCCTTTGCGTGTTATATTGCCTTGAGGCGATTCGTGGCTCCGGAGGCAAAAACTCCGTATACGGGTTTAGCCCGTATGGTAAACCTGGGCTCGAATCGGGCTGGTACAAGCGTCTTGTTCTACGATGTTCAATTCGAGACGGCCTCGACTATCCAGCACTATGAGGCACTATTCGGTTACCTTCACATTGACCTTCTACCGAGAGTTCATTCTCACTCCACGTTAAAGTCTGGATAA
>Rosalind_2984
AGACGAGGCCATTCTTCCATCAAGAACCTCGGACCCAGGACCGGCCT
>Rosalind_7447
GCCCGTATGGTAAACCTGGGCTCGAATCGGGCTGG
>Rosalind_9937
CTTAAAGTCACCCCTACCCTCA
>Rosalind_9249
GCGCATGTATGTTTG
>Rosalind_3123
ACCAGTCGTTCCAGTCATGCTCTA
>Rosalind_3585
GGTTACCGTATGGAGCG
>Rosalind_4716
TCTCACCGACAGGCCCAAGGGCTTGAAGGATGCGGCA
>Rosalind_2392
GGCCTCGACTATCCAGCACTATGAGGCACTATTCGGTTACCTTCACATT
>Rosalind_4870
AGAATCGGGCCCAGA
>Rosalind_2900
CCTTGAGGCGATTCGTGGCT
>Rosalind_0289
GCACTGCGATTTCTGCGTGAGCCAGACAACT
>Rosalind_5439
CGACTTGTATTCGCCTGGATACCAATTACATCTT
>Rosalind_7492
CCGGTGCCGGTAGAGCGTGTAGTTTGATTGTCCGGGACC
>Rosalind_6849
CGGTTGATCCGTCCCATCACGAAATGAAAACAATCTA
""".split()[1::2]

for i in range(len(input)):
	input[i] = input[i].replace('T','U') 
	
phrase = input[0] #Main sequence
introns = input[1:] #Get list of introns

for i in introns:
	phrase = phrase.replace(i, '')
	
proteinString = ""
string = ""
i = 0
for i in range(len(phrase)):
	string += phrase[i]
	if len(string) == 3:
		proteinString += codonTable[string]
		string = ""
		
print proteinString
