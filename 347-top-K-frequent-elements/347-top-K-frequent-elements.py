import collections, heapq

class Solution:
    def topKFrequent(self, nums, k: int):
        if not nums or len(nums)==1:
            return nums
        
        freq_dict = collections.Counter(nums)
        
        h = []
        for key, value in freq_dict.items():
            heapq.heappush(h, (-value, key))
        
        ans = []
        for i in range(k):
            value = heapq.heappop(h)[1]
            ans.append(value)
        
        return ans