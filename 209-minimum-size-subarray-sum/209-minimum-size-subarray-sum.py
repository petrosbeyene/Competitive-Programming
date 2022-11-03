class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        beg_p = 0
        prefSum = 0
        ans = len(nums)+1
        for i in range(len(nums)):
            prefSum += nums[i]
            while prefSum >= target:
                ans = min(ans, i+1-beg_p)
                prefSum -= nums[beg_p]
                beg_p += 1
        
        return ans if ans != len(nums)+1 else 0