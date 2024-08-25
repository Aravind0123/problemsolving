class Solution(object):
    def merge(self,nums1, m, nums2, n):
        n=m+n
        num = nums1 + nums2
        nums=[]
        for i in num:
            if i!=0:
                nums.append(i)
        for i in range(n):
            for j in range(n-i-1):
                    if nums[j]>nums[j+1]:
                        nums[j],nums[j+1]=nums[j+1],nums[j]
        print(nums)
        
            
nums1 = [1,2,3,0,0,0]
m=3
nums2 = [2,5,6]
n = 3
Solution().merge(nums1,m,nums2,n)
        