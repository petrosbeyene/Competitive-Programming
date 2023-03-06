class Solution:
    def mySqrt(self, x: int) -> int:        
        beg = 1
        end = x
        while beg <= end:
            mid = beg + (end - beg)//2
            if mid*mid == x:
                return mid 
            elif mid*mid < x:
                beg = mid + 1
            else:
                end = mid - 1
        
        return end