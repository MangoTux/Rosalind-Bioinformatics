import operator
#def Main():
s,t=open('input.txt').read().split('\r\n')
print sum(map(operator.ne, s, t))#getHammingDistance(s,t)
#def getHammingDistance(s, t): #Number of differences between two identical strings
#	hD = 0
#	for i in range(len(s)):
#		if s[i] != t[i]:
#			hD+=1
#	return hD

#if __name__ == "__main__":
#	Main()