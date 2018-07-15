#!/usr/bin/python
from __future__ import print_function
import re, sys


d_to_l = dict()

def gen_dict():
	global d_to_l
	i = 97
	d = 2
	while(i<123):
		if (d!=7) and (d!=9):
			s = chr(i) + chr(i+1) + chr(i+2)
			i+=3
		else:
			s = chr(i) + chr(i+1) + chr(i+2) + chr(i+3)
			i+=4
		d_to_l[str(d)] = s
		d+=1



def gen_comb(s):
	lst = [""]
	for i in s:
		temp_lst = []
		if ord(i)<50 or ord(i)>57:
			return -1 
		for c in d_to_l[i]:
			for l in lst:
				new_s = l+c
				temp_lst.append(new_s)
		lst = temp_lst
	return lst

if __name__ == "__main__":
	gen_dict()
	map(print, gen_comb(sys.argv[1]))
#	print(d_to_l)
	
