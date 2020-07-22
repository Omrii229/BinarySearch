__version__=0.1
__author="Omri"

def get_input():
	A=input("Enter numbers:\n").split(' ')
	A=[n for n in A if n.isdigit()]
	return sorted(A)
	
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
	

def main():
	A=get_input()
	num=""
	while(not num.isdigit()):
		num=input("What number to search? ")
	index=bin_search(A,num,len(A)-1,0)
	if index != -1:
		print("Found at index {0}".format(index))
	else:
		print("Not Found")
	

if __name__=="__main__":
	main()