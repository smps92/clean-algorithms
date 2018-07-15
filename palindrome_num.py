#!/usr/bin/python


def check_palindrome(s):
	len_s = len(s)
	for i in range(len_s):
		if s[i]!= s[len_s-i-1]:
			return False
	return True

if __name__ == "__main__":
	num_str = sys.argv[1]
	n = int(num_str)
	if n<0:
		print("not palindrome")
	else:
		if check_palindrome(num_str) else print("not palindrome")
