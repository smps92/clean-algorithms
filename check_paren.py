#!/usr/bin/python
import sys


lst = []

def check_balanced(paren_string):
	for s in paren_string:
		if s == '(':
			lst.append(0)
		elif s == ')':
			if len(lst) == 0:
				return -1
			lst.pop(0)
		else:
			return -1
	if len(lst) == 0:
		return 1
	else:
		return -1
		
			
#def check(paren_string):
#	global n
#	if (len(paren_string) == 0) and (n!=0):
#		return -1
#	if paren_string[0] == '(':
#		n+=1
#		return check(paren_string[1:])
#	else paren_string[0] == ')':
#		n-=1
#		return check(paren_string[1:])

if __name__ == "__main__":
	paren_string = sys.argv[1]
	print(check_balanced(paren_string))
