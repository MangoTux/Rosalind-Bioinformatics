import urllib2
import urllib
import re
input = """
Q66GC7
P01047_KNL2_BOVIN
Q67JS9
A9QYR8
Q3BRP8
Q5PA87
P12763_A2HS_BOVIN
B3CNE0
P01044_KNH1_BOVIN
P17404_CHM1_BOVIN
P05783_K1CR_HUMAN
Q50228
P01787
P01876_ALC1_HUMAN
P0A4Y7
""".split()

##We're searching for the N-glycosylation motif, defined as N{P}[ST]{P}, which is N, not P, S or T, not P.
##Can be defined as a regular expression N[^P]{1}[ST][^P]{1}
def searchGlycosylation(sequence):
	r = re.compile("N[^P]{1}[ST][^P]{1}")
	list = []
	for i in range(len(sequence)):
		if r.match(sequence[i:i+4]):
			list.append(int(i)+1)
	return list

##Gets the protein sequence of a given fasta code by delimiting the header.
def getProteinSequence(s):
	try:
		response = urllib2.urlopen("http://www.uniprot.org/uniprot/" + s + ".fasta")
		html = ''.join(response.read().split('\n')[1::]).strip() #Get the entire code of the sequence sans header info
		return searchGlycosylation(html)
	except urllib2.URLError as e:
		print e.reason
	

def Main():
	for s in input: #Iterate through the proteins in the list to find sequences with the N-glycosylation motif.
		indexList = getProteinSequence(s) #Gets the list of indices of N-glycosylation motif if it exists in a given sequence
		if len(indexList) > 0:
			print s
			for i in indexList:
				print i, 
			print ""
			
if __name__ == "__main__":
	Main()