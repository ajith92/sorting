def insertion_sort(nums):
	for i in range(1,len(nums)):
		a=nums[i]
		j=i-1
		while j>=0 and nums[j]>a:
			nums[j+1]=nums[j]
			j-=1
		nums[j+1]=a
	
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
	nums=insertion_sort(nums)
	#print sorted data
	print "sorted data is : ",nums
 
