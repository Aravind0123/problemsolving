
class Solution:
    def rotate(self, nums, k) -> None:
        def reverse(i: int, j: int):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i + 1, j - 1

        n = len(nums)
        k = 4
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
        print(nums)
nums=[1,2,3,4,5]
k=3
Solution().rotate(nums,k)