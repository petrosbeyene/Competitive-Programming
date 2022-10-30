class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        if i >= 0:     
            j = len(nums) - 1
            while j > i:
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
                j -= 1
                
        nums[i+1:] = nums[i+1:][::-1]      