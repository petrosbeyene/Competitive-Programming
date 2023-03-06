from math import ceil

class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        
        def canEat(pos_k, h):
            hrs = 0
            for p in piles:
                hrs += (ceil(p/pos_k))
                print
            return True if hrs <= h else False

        low = 1
        min_k = high = max(piles) 
        while low <= high:
            mid = low + (high - low)//2
            if canEat(mid, h):
                min_k = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return min_k