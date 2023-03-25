class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        #Cyclic Sorting implementation
        n = len(nums)
        i = 0
        ans = []
        while i < n:
            if nums[i] == -1 or i == nums[i]-1:
                i += 1
                continue
            
            corr_idx = nums[i] - 1
            if nums[i] == nums[corr_idx]:
                ans.append(nums[i])
                nums[i] = -1
                continue
            else:
                nums[i], nums[corr_idx] = nums[corr_idx], nums[i]
        
        for idx, val in enumerate(nums):
            if val == -1:
                ans.append(idx+1)
        
        return ans

        #Time Complexity: O(n)
        #Space Complexity: O(1) disregarding the space for ans array

