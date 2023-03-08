class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l, r = 0, k
        maxSum = total = sum(nums[0:k])
        while r < len(nums):
            total = total - nums[l] + nums[r]
            maxSum = max(maxSum, total)
            l += 1
            r += 1
        
        return maxSum/k
