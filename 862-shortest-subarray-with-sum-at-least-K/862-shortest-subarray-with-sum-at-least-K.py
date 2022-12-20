import collections

class Solution:
    def shortestSubarray(self, nums, k: int) -> int:
        pref_sum = [0]
        for num in nums:
            pref_sum.append(pref_sum[-1]+num)
        
        deq = collections.deque()
        ans = float('inf')
        for i, curr_sum in enumerate(pref_sum):
            while deq and deq[-1][1] >= curr_sum:
                deq.pop()
            deq.append([i, curr_sum])
            
            while deq and curr_sum - deq[0][1] >= k:
                ans = min(ans, i - deq[0][0])
                deq.popleft()
        
        return ans if ans != float('inf') else -1