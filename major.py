nums=[2,1,1,3,3,3]
majority = nums[0]
count=0
n=len(nums)
for i in range(n-1):
    if(majority==nums[i]):
        count=count+1
    elif(count<=0):
        majority=nums[i]
    else:
        count=count-1
print(majority)