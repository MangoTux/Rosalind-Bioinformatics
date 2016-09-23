import itertools

input = 7
#Wow python is cool - creates all possible permutations in range of input
perm = list(itertools.permutations(range(1,input+1)))
print len(perm)
for x in perm:
	for y in x:
		print y,
	print ""