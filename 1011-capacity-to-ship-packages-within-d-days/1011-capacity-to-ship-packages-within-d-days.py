class Solution:
    def shipWithinDays(self, weights, days: int) -> int:
        
        def isValidWeight(weight):
            cnt = 0
            tot_w = 0
            for w in weights:
                tot_w += w
                if tot_w >= weight:
                    cnt += 1
                    tot_w = 0 if tot_w == weight else w
            if tot_w > 0:
                cnt += 1
            return True if cnt <= days else False
        
        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = low + (high - low)//2
            if isValidWeight(mid):
                high = mid -1
            else:
                low = mid + 1
        
        return low