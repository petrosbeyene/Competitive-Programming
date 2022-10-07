import collections
class Solution:
    def longestSubarray(self, nums, limit: int) -> int:
        #deque to cointain all maximum elements in monotonical decreasing order
        maxdeque = collections.deque()
        
        #deque to contain all minimun elements in monotonically increasing order
        mindeque = collections.deque()
        
        i = 0
        for num in nums:
            while len(maxdeque) and num > maxdeque[-1]:
                maxdeque.pop()
            while len(mindeque) and num < mindeque[-1]:
                mindeque.pop()
            
            maxdeque.append(num)
            mindeque.append(num)
            
            if maxdeque[0] - mindeque[0] > limit:
                if maxdeque[0] == nums[i]:
                    maxdeque.popleft()
                if mindeque[0] == nums[i]:
                    mindeque.popleft()
                i += 1
        
        return len(nums) - i
					
