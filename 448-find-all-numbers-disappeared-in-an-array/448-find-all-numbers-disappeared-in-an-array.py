class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == -1 or i == nums[i]-1:
                i += 1
                continue
            
            corr_pos = nums[i] - 1
            if nums[i] == nums[corr_pos]:
                nums[i] = -1
                continue
            else:
                nums[corr_pos], nums[i] = nums[i], nums[corr_pos]
        
        ans = []
        for i in range(n):
            if nums[i] == -1:
                ans.append(i+1)
        
        return ans
