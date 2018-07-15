#!/usr/bin/python
from __future__ import print_function
import sys


def get_digits(n):
	digits = []
	while(n>0):
		d = n%10
		n = n/10
		digits.append(d)
	return digits


def permutations(string):
#	digits = get_digits(n)
	digits_s = string
	lst = [""]
	for (i,d) in enumerate(digits_s):
		temp_list = []
		for l in lst:
			len_l = len(l)
			for i in range(0,len_l+1):
				temp_list.append(l[:i] + d + l[i:])
		lst = temp_list
	perm_dict = { perm:1 for perm in lst}
	return perm_dict


if __name__ == "__main__":
	s = sys.argv[1]
	map(print, permutations(s).keys())
