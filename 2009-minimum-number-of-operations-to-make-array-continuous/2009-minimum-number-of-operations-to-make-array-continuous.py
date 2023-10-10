class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        n = len(nums)
        nums = sorted(set(nums))
        ans = float("inf")
        for i, start in enumerate(nums):
            end = start + n - 1
            end_corr_place = bisect_right(nums, end)

            ans = min(ans, n - (end_corr_place - i))
        
        return ans
