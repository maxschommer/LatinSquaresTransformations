import numpy as np 
from matplotlib import pyplot as plt




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

def genMultiset(n):
	pass

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
	latinSquares = findAllLatinSquaresBF(3)
	print(len(latinSquares))


if __name__ == '__main__':
	main()