import sys

def prim_root(value):    
 # `tot` gets the list of values coprime to the input,
 # so len(tot()) is the correct totient value 
	totient = tot(value) 
	roots = []
	exp = len(totient) 
	for x in totient:
		y = 1   
		while pow(x, y, value) != 1:# i forget exactly why i did this    
			y += 1              # i think it was because of the     
			if y == exp:                # period of the mod value         
				roots += [x]     
	return roots

def gcd(a, b):
	a, b = max(a, b), min(a, b) 
	c = 1  
	while c:    
		c = a % b    
		a = b   
		b = c 
	return a

def tot(n):  
	phi = [] 
	x = 1  
	while x < n:# not for x in xrange(n) because the input is too big for xrange      
		if gcd(x, n) == 1:        
			phi += [x]      
		x += 1  
	return phi

print prim_root(int(sys.argv[1]))