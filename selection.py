def selection_sort(nums):
	for i in range(len(nums)):
		minv=i
		for j in range(i+1,len(nums)):
			if nums[j]<nums[minv]:
				minv=j
		temp=nums[i]
		nums[i]=nums[minv]
		nums[minv]=temp
								
	return nums

def get_data():
	nums=[]
	while True:
		a=int(raw_input("Enter a number (-1 if done) : "))
		if a==-1:
			break
		nums.append(a)
	return nums

if __name__=='__main__':
	#collect data
	nums=get_data()
	#print input data
	print "Input data is : ",nums
	#sort data
	nums=selection_sort(nums)
	#print sorted data
	print "sorted data is : ",nums
 
