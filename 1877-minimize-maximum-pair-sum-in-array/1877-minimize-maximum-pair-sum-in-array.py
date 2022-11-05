class Solution:
    def minPairSum(self, nums) -> int:
        nums.sort()
        
        i = 0
        j = len(nums)-1
        minimized_max_pair = 0
        while i < len(nums)//2:
            minimized_max_pair = max(minimized_max_pair, nums[i]+nums[j])
            i += 1
            j -= 1
        
        return minimized_max_pair