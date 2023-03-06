from math import ceil


class Solution:
    def smallestDivisor(self, nums, threshold: int) -> int:
        def isValidDivisor(d):
            tot = 0
            for n in nums:
                tot += (ceil(n/d))
            
            if tot <= threshold:
                return True
            else:
                return False
        
        low, high = 1, max(nums)
        while low <= high:
            mid = low + (high - low)//2
            if isValidDivisor(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return low