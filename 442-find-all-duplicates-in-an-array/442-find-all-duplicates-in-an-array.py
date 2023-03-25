class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        ans = []
        #Cyclic Sort implementation
        while i < n:
            if nums[i] == -1 or i == nums[i]-1:
                i += 1
                continue
            
            corr_pos = nums[i] - 1
            if nums[i] == nums[corr_pos]:
                ans.append(nums[i])
                nums[i] = -1                
                continue
            else:
                nums[corr_pos], nums[i] = nums[i], nums[corr_pos]
        
        return ans
        
        #Time Complexity: O(n)
        #Space Complexity: O(1), without considering the space for ans
