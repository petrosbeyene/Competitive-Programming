class Solution:
    def maxFrequency(self, nums, k: int) -> int:
        nums.sort()
        left = 0
        right = maxfreq = 1
        windowSum = nums[0]
        while right < len(nums):
            windowSum += nums[right]
            while nums[right]*(right-left+1) - windowSum > k:
                windowSum -= nums[left]
                left += 1
            maxfreq = max(maxfreq, (right-left+1))
            right += 1
        
        return maxfreq