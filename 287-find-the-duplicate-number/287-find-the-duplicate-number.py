class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Cyclic Sort Implementation
        n = len(nums)
        i = 0
        while i < n:
            if i == nums[i]-1:
                i += 1
                continue
            
            corr_idx = nums[i] - 1
            if nums[i] == nums[corr_idx]:
                return nums[i]
            else:
                nums[i], nums[corr_idx] = nums[corr_idx], nums[i]
        
        #Time Complexity: O(n)
        #Space Complexity: O(1)
