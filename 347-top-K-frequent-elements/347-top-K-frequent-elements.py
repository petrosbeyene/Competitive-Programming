import heapq


class Solution:
    def topKFrequent(self, nums, k: int):
        if not nums or len(nums)==1:
            return nums
        
        freq_dict = {}
        for num in nums:
            if num in freq_dict:
                freq_dict[num] -= 1
            else:
                freq_dict[num] = -1
        
        h = []
        for key in freq_dict:
            heapq.heappush(h, (freq_dict[key], key))
        
        ans = []
        cnt = 1
        while cnt <= k:
            freq, value = heapq.heappop(h)
            ans.append(value)
            cnt += 1
        
        return ans
            