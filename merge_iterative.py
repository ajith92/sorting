def merge_sort(nums):
  """ THIS ALGO IS INCOMPLETE....WORKED ON IT, BUT STILL DINT FINISH IT
		NEEDED SOME MORE TIME TO FINISH (im just there)"""
	buff=[]
	i=0	#index for 1st half in merge
	j=0	#index for 2nd half in merge
	for iaddfac in list[2**z for z in range(1,15)]:
		if i+iaddfac<len(nums):
			
			jaddfac=iaddfac/2
			j=i+jaddfac
			while i<i+jaddfac and j<j+jaddfac:
				if nums[i]<nums[j]:
					buff.append(nums[i])
				else:
					buff.append(nums[j])
			if i<i+jaddfac:
				buff+=nums[i:i+jaddfac]
			else:
				buff+=nums[j:j+jaddfac]
		else:
			return buff		
			
		  

def  get_data():
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
	nums=merge_sort(nums)
	#print sorted data
	print "sorted data is : ",nums
 
