class Solution(object):
    def removeDuplicates(self, nums):
        k = 0
        for x in nums:
            if k == 0 or x != nums[k - 1]:
                nums[k] = x
                k += 1
        return k
nums=[1,1,2]
sorted = Solution().removeDuplicates(nums)
print(sorted)

       
        