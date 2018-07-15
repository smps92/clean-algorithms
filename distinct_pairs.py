#!/usr/bin/python
from __future__ import print_function
import sys


#def get_key(number, t):
#	if number > t:
#		return str(t)+"_"+ str(number)
#	else:
#		return str(number)+"_" + str(t)


def get_key(number, t):
	return str(min(t, number))+ "_"+str(max(t,number))

def print_count_pairs(numbers, target):
	numbers_dict = {}
	for number in numbers:
		try:
			numbers_dict[number]+=1	
		except KeyError:
			numbers_dict[number] = 1
#	print(numbers_dict)
	sum_to_target_dict = {}
	for number in numbers_dict.keys():
		t = target - number
		key = get_key(number, t)
		if (number == t):
			if (numbers_dict[number]>1):
				sum_to_target_dict[key] = 1
		elif t in numbers_dict:
				sum_to_target_dict[key] = 1
#		print(sum_to_target_dict)
	return len(sum_to_target_dict.keys())

if __name__ == "__main__":
	with open(sys.argv[1], "r") as fd:
		for line in fd:
			(target, numbers_str) = line.split(":")
			numbers = [int(number_s) for number_s in numbers_str.split(" ")]
			print(print_count_pairs(numbers, int(target)))
	
