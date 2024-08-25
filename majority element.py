from itertools import count

class Solution(object):
    def majorityElement(self, nums):
        for i in nums:
            x= count(i)
            y= len(nums)//2
            k= x>=y
            
nums=[1,1,2,2,2]
sol= Solution().majorityElement(nums)
print(sol)
            
                
        