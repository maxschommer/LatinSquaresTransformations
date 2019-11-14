import numpy as np 
from matplotlib import pyplot as plt



def genNaryString(n, els_left=None, res_str="", res_arr=[]):
	if els_left == None:
		els_left = n**2-1
	# res = []
	for i in range(n):
		if els_left <= 0:
			res_arr.append(res_str + "{}".format(i))
		else:
			res_arr.append(genNaryString(n, els_left-1, res_str +  "{}".format(i), res_arr))
		# 	res.append(genNaryString(n, els_left-1, [i]))
	return res_arr

# Find latin squares with a brute force method, iterating through 
# all possible matrices, simply checking conditions of latin squarness
def findLatinSquaresBruteForce(n):
	arr = np.ones((n,n))

	numSquares = n**(n**2)
	for sqNum in numSquares:
		# TODO: Figure out how to generate all possible matrices
		pass

	# 		for k in range(n):
	# 			arr[i,j] = k +1
	# 			print(arr)


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
		for elt in row:
			if (not elt in isIn) and elt <= size:
				isIn[elt] = True
			else:
				return False
	return True



def main():
	testSquare = np.asarray([[1,2,3],
							[2,3,1],
							[3,1,2]])
	isSquare = checkSquare(testSquare)
	print(isSquare)

	# findLatinSquaresBruteForce(3)
	strs = genNaryString(2)
	print(strs)

if __name__ == '__main__':
	main()