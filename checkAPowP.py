#!/usr/bin/python
import sys
import math


def f(x,a,p):
	return math.pow(x,p) - a

def f_dash(x,a,p):
	return p*math.pow(x,p-1)

def newton(n):
	numiter = 10
	maxP = math.log(n)/math.log(2)
	for i in range(maxP,2, -1):
		iter_count = 0
		root_i = 2
		while(iter_count<numiter):
			root_iPlus1 = root_i + f(root_i, n,i)*1.0/f_dash(root_i, n, i)
		probable_pth_root = int(root_iPlus1)
		if math.pow(probable_pth_root, i) == n:
			return True
	return False
	
def checkAPowP(n):
	for i in range(2,int(math.sqrt(n))+1):
		temp = i
		while(temp<n):
			temp*=i
		if temp == n:
			return True
	return False


if __name__ == "__main__":
	n = int(sys.argv[1])
	if n == 0:
		print(0, False)
	if n == 1:
		print(1, True)
	if n == 2:
		print(2, False)
	else:
		print(n, checkAPowP(n))
