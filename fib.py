#Rabbits and Recurrence Relations
input = "32 4" # n <= 40 := generations, k <= 5 := number of offspring pairs

def Main():
	n = int(input.split()[0])
	k = int(input.split()[1])
	print fib(n-1, k)

#Modified fibonacci for rabbits producing k offspring after n months
def fib(n, k):
	if n == 1 or n == 0:
		return 1
	else:
		return fib(n-1, k) + k*fib(n-2, k) #Standard fib -> Change recurrence
		
if __name__ == "__main__":
	Main()