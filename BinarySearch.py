__version__=0.1
__author="Omri"

import random

FROM=1
TO=100
ELEMENTS=5
def get_input():
	A=input("Enter numbers:\n").split(' ')
	A=[n for n in A if n.isdigit()]
	return list(map(int,sorted(A)))
	
def bin_search(A,num,high,low):
	if high>=low:
		middle_index=(high+low)//2
		if A[middle_index]==num:
			return middle_index
		elif A[middle_index]>num:
			return bin_search(A,num,middle_index-1,low)
		else:
			return bin_search(A,num,high,middle_index+1)
	else:
		return -1
	
def random_generate():
	A = random.sample(range(FROM, TO), ELEMENTS)
	return sorted(A)

def main():
	choice=''
	while not choice.isdigit():
		choice=input("1 - Insert manually numbers , 2 - Random:\n")
		if choice.isdigit() and int(choice) not in range (1,3):
			choice=''
	if choice == "1":
		A=get_input()
	else:
		A=random_generate()
	num=""
	while not num.isdigit():
		num=input("What number to search? ")
	index=bin_search(A,int(num),len(A)-1,0)
	if index != -1:
		print("Found at index {0}".format(index))
	else:
		print("Not Found")
	

if __name__=="__main__":
	main()