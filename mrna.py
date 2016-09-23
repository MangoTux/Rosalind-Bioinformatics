codonTable = """
UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G """

elements = codonTable.strip().split()[1::2]
input = open('input.txt').readline().strip()
d = {}
for i in elements:
	if i in d:
		d[i] += 1
	else:
		d[i] = 1
total = 1
for i in range(len(input)):
	total *= d[input[i]]
	total %= 1000000
total *= 3
total %= 1000000 #Stop bit
print total