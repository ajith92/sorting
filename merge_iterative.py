def merge_stage(nums,iaddfac):
    buffer=[]
    jaddfac=iaddfac/2
    i=0
    j=i+jaddfac
    while i<len(nums) or j<len(nums):
        while i<i+jaddfac and j<j+jaddfac:
            if nums[i]<nums[j]:
                buffer.append(nums[i])	
                i+=1
            else :
                buffer.append(nums[j])
                j+=1		
        if i<i+jaddfac:buffer+=nums[i:i+jaddfac]
        else:buffer+=nums[j:j+jaddfac]	
        i=i+iaddfac
        j=i+jaddfac
    if i<len(nums):
        buffer+=nums[i:len(nums)]
    return buffer

def merge_sort(nums):
    list1=[2**z for z in range(1,15)]
    for iaddfac in list1: 
        if iaddfac/2 < len(nums):
            nums=merge_stage(nums,iaddfac)
        else: break 
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
	nums=merge_sort(nums)
	#print sorted data
	print "sorted data is : ",nums
raw_input("Enter to exit :" )
