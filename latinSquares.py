import numpy as np 
from matplotlib import pyplot as plt

from sympy.utilities.iterables import multiset_permutations


# Generate all strings of length n**2 made with n symbols.
# TODO: Make this function able to work one at a time using 
# modular arithmetic.
def genNaryString(n, els_left=None, res_str=[], res_arr=[]):
	if els_left == None:
		res_arr = [] # For some reason this needs to be reset
		els_left = n**2-1
	for i in range(n):
		next_res_str = [*res_str, i]
		if els_left <= 0:
			res_arr.append(next_res_str)
		else:
			genNaryString(n, els_left-1, next_res_str, res_arr)
	return res_arr

# Generate the set of all permutations of size n.
def genMultiset(n):
	a = np.arange(n)
	return list(multiset_permutations(a))

# Generate all derangements of an input vector.
def getDerangements(inputs):

	perms = genMultiset(len(inputs))
	res = []
	for perm_try in perms:
		isDer = True
		for i in range(len(perm_try)):
			if inputs[i] == perm_try[i]:
				isDer = False
		if isDer:
			res.append(perm_try)
	return res

# NOTE: Currently an experimental function that's not
# fully implemented, and doesn't mean what it's function name
# means. 
def numDerangements(n, depth):
	perms = genMultiset(n)
	permsDeranged = getDerangements(n)
	print(permsDeranged)
	# Note: It depends on whether you loop through perms or 
	# permsDeranged first whether the len(ans) is consistent
	accum = 0
	for perm in perms:
		res = []
		for perm_try in permsDeranged:
			isDer = True
			# print("Perms: ", perm, perm_try)
			for i in range(len(perm_try)):
				if perm[i] == perm_try[i]:
					isDer = False
			if isDer:
				res.append(perm_try)
				accum = accum + 1
		print(len(res))
	print(accum)

# Find matrices of size nxn with integers 0 to n-1
def findAllMatrices(n):
	squareArrays = genNaryString(n)
	# print(len(squareArrays))
	res = []
	for sqNum in squareArrays:
		# print(sqNum)
		res.append(np.reshape(sqNum, (n, n)))
	# print("Res Length: ", len(res))
	return res

# Finds all Latin Squares using a brute force method, simply 
# checking if each possible matrix is a latin square.
def findAllLatinSquaresBF(n):
	squareArray = findAllMatrices(n)
	res = []
	for square in squareArray:
		if checkSquare(square):
			res.append(square)
	return res

# Finds all Latin Squares using finesse force. Slightly more elgant than
# brute force.
def findAllLatinSquareFF(n):
	pass


# Find out how many derangements exist that satisfy the criteria of
# multiple 
def multiDerrangement(inputs):
	x, n = inputs.shape()


# Checks whether an nxn matrix is a latin square.
def checkSquare(Sq):
	(size, _) = Sq.shape

	for row in Sq:
		isIn = {}
		for elt in row:
			if (not elt in isIn) and elt <= size:
				isIn[elt] = True
			else:
				return False

	for col in np.transpose(Sq):
		isIn = {}
		for elt in col:
			if (not elt in isIn) and elt <= size:
				isIn[elt] = True
			else:
				return False
	return True



def main():
	# latinSquares = findAllLatinSquaresBF(3)
	# print(len(latinSquares))

	# perms = 
	
	ders = getDerangements(np.array([0,1,2,3]))
	print(ders)

	# ders = numDerangements(4, 1)
	# # print(len(ders))



if __name__ == '__main__':
	main()