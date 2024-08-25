class Solution(object):
    def removeElement(self, nums, val):
        k=0
        for i in nums:
            if i!=val:
                nums[k]=i
                k=k+1
        return k

nums=[0,1,2,2,3,0,4,2]
val=2
num=Solution().removeElement(nums,val)
print(num)
