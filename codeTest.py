problem = """
Given two lists A and B, return two lists that contain:
(1) All elements in A not found in B
(2) All elements of B with duplicates
"""

# A different method of solving this concurrently
def problemSolution(A, B):
	dict2 = {}
	#Fill up array
	for i in B:
		if i in dict2:
			dict2[i] += 1
		else:
			dict2[i] = 1
	return [x for x in A if not x in B], [y for y in dict2 if dict2[y] > 1]
	
l1, l2 = problemSolution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 4, 6, 8, 8, 10])
print l1
print l2