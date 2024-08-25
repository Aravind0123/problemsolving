nums=[2,3,-2,-2,-1,23]
n=len(nums)
def maxsubarray(nums):
    max=0
    for i in range(n):
        for j in range(i+1,n):
            lst=nums[i]*nums[j]
            if max<lst:
                max=nums[i]*nums[j]
                return (nums[i],nums[j])
print( maxsubarray(nums))

    