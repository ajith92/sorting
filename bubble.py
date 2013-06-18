def bubble_sort(nums):
	for i in range(len(nums)):
		for j in range(0,len(nums)-i-1):
			if nums[j]>nums[j+1]:
				temp=nums[j]
				nums[j]=nums[j+1]
				nums[j+1]=temp				
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
	nums=bubble_sort(nums)
	#print sorted data
	print "sorted data is : ",nums
 
