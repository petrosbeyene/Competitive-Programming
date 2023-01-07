class Solution:
    def longestSubarray(self, nums) -> int:
        k = 1
        left = 0
        ans = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            
            ans = max(ans, right-left)
        
        return ans