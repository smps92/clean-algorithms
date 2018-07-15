#!/usr/bin/python
from __future__ import print_function
import sys
import math
import re

def get_bin_rep(i , n):
	lst = []
	count = 0
	while(i>0):
		lst.append(str(i%2))
		i/=2
		count+=1
	num_zeros_to_append = int(math.ceil(math.log(n) - count +1))
	lst.reverse()
	temp = "".join(lst)
	temp = "0"*num_zeros_to_append + temp
	return "".join(temp)

def gen_all_binary(n):
	lst = list()
	for i in range(1,n):
		lst.append(get_bin_rep(i,n))
	lst.append("0"* int(math.ceil(math.log(n) +1)))
	return lst

def gen_all_paren(n):
	lst = gen_all_binary(n)
	new_list = list()
	for string in lst:
		temp = re.sub(r'0',')',string)
		temp = re.sub(r'1','(',temp)
		new_list.append(temp)
	return new_list
		

if __name__ == "__main__":
	n = int(sys.argv[1])
	map(print, gen_all_binary(pow(2,2*n)))
	#print(get_bin_rep(n,n))
