#!/usr/bin/python
from __future__ import print_function
import sys



def rem_dup(numbers):
	i = 0
	count = len(numbers)
	while(i<count):
		num = numbers[i]
		j = i+1
		while((numbers[j] == num) and (j<count)):
			j+=1
		if j<count:
			numbers[i+1] = numbers[j]
		i = j
	for p in range(i+1,n):
		numbers[p] = 0;
	return i


if __name__ == "__main__":
	with open(sys.argv[1], "r") as fd:
		for line in fd:
			numbers = [i for i in line.split(" ")]
			print(rem_dup(sorted(numbers)))
	
