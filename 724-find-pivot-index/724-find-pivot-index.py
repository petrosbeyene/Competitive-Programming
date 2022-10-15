class Solution:
    def pivotIndex(self, nums) -> int:
        prefix_sum = [0]*len(nums)
        prefix_sum[0] = nums[0]
        
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
            
    
        prefix_sum.insert(0, 0)
        prefix_sum.append(0)
        
        n = len(prefix_sum)
        tot = sum(nums)
        for i in range(1, n-1):
            if prefix_sum[i-1] == tot - prefix_sum[i]:
                return i-1
        return -1