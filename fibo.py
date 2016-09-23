i = 20

a = b = 1
for j in range(i-1):
	a, b = a+b, a
print b