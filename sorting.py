nums1 = [1,5,6,8,6]
nums2 = [5,9,8,11]
nums = nums1 + nums2 
print("After Adding:" , nums)
n = len(nums)
for i in range(0,n) :
    for j in range(0,n-i-1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
print("After Sorting : " ,nums)
new_nums =[]
for i in nums:
    if i not in new_nums:
        new_nums.append(i)
print("After Removing Duplicates" , new_nums)
