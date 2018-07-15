#!/usr/bin/python
import sys


def match(char s, char c):
	if (s == '}') and (c == '{'):
		return True
	if (s == ')') and (c == '('):
		return True
	if (s == ']') and (c == '['):
		return True
	return False
		

def check_paren(paren_string):
	lst = []
	for s in  paren_string:
		if s in ('{', '(','['):
			lst.append(s)
		if s in (')','}',']'):
			popped = lst.pop()
			if match(s,popped) is not True:
				return -1
		else:
			return -1
	return 1
	

if __name__ == "__main__":
	paren_string = sys.argv[1]
	check_paren(paren_string)
