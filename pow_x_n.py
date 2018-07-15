#!/usr/bin/python
from __future__ import print_function
import sys
import math
d = dict()

def pow_x_n(x, n):
	if  n in d:
		return d[n]
	if n == 1:
		d[n] = x
		return d[n]
	else:
		c = math.ceil(n/2.0)
		f = math.floor(n/2.0)
		term_1 = pow_x_n(x, c)	
		term_2 = pow_x_n(x, f)
		d[n] = term_1*term_2
		return d[n]

def act_pow(x,n):

	if n == 0:
		return 1
	if x == 0:
		return 0
	if x == 1:
		return 1
	if x == -1:
		return 1 if n%2 == 0 else -1
	abs_x = math.fabs(x)
	abs_n = math.fabs(n)
	sign = 1 if x>0 else 1 if n%2 == 0 else -1
	powxn = pow_x_n(abs_x, abs_n)
	if n<0:
		return sign * 1.0/powxn
	if n>0:
		return sign * powxn


if __name__ == "__main__":
	x = int(sys.argv[1])
	n = int(sys.argv[2])
	print(act_pow(x,n))
