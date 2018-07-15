#!/usr/bin/python
from __future__ import print_function
import sys

def equals(s,t):
	if len(s) != len(t):
		return False
	else:
		j = 0
		while((s[j] == t[j])):
			j+=1
			if j == len(s):
				break
		if j<len(s):
			return False
		else:
			return True

def strstr(n, h):
	if len(h) < len(n):
		return -1
	if len(n) < 1:
		return -1
	len_n = len(n)
	gen_substr = { h[i:i+len_n]:i for i in range(len(h))}
	for substr in gen_substr.keys():
		if equals(substr,n):
			return gen_substr[substr]
	return -1

def strstr_1(n, h):
	len_h = len(h)
	len_n = len(n)
	if len_h < len_n:
		return -1
	if len_n < 1:
		return -1
	found = False
	i = 0
	while not found:
		if n[i] != h[i]:
			i+=1
		else:
			j = 0
			while(n[j] == h[i+j]):
				j+=1	
				if j == len_n:
					break
			if j == len_n:
				return i
			else:
				i+=1
				
				
		

def run_all_testcases(filename):
	with open(filename, "r") as fd:
		for line in fd:
			(needle, haystack) = line.split(" ")
			print(strstr(needle, haystack))
	

if __name__ == "__main__":
#	print(equals(sys.argv[1], sys.argv[2]))
	print(strstr(sys.argv[1], sys.argv[2]))
