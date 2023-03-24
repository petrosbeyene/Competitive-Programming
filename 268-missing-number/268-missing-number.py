class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        i = 0
        while i < n:
            if nums[i] == -1 or i == nums[i]:
                i += 1
                continue
            
            corr_pos = nums[i]
            if corr_pos >= n:
                nums[i] = -1
                continue
            else:
                nums[corr_pos], nums[i] = nums[i], nums[corr_pos]
        
        for i in range(n):
            if nums[i] == -1:
                return i
        
        return nums[-1]+1
        
