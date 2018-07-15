#!/usr/bin/python
from __future__ import print_function
import sys
import re


def s_replace(string, pat):
	lst = []
	for match in re.finditer(r's', string):
		lst.append(string[:match.start()] + pat + string[match.end():])
	return lst

	
def gen_paren(n):
	base_map = { "s":1 }
	for i in range(n-1):
		temp_list = []
		for paren_string in base_map.keys():
			replaced_list = s_replace(paren_string, '(s)')
			for replaced in replaced_list:
				temp_list.append(replaced)
			replaced_list = s_replace(paren_string, 'ss')
			for replaced in replaced_list:
				temp_list.append(replaced)
#		print_paren_strings(temp_list)
		base_map = { i:1 for i in temp_list}
	new_list = []
	for paren_string in base_map.keys():
		new_list.append(re.sub(r's','()', paren_string))
	return new_list
	
def print_paren_strings(lst):
	map(print, lst)
#	print(lst)


if __name__ == "__main__":
	n = int(sys.argv[1])
	paren_strings = gen_paren(n)
	print_paren_strings(paren_strings)
	
