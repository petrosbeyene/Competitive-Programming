from collections import Counter


class Solution:
    def topKFrequent(self, nums, k: int):
        if not nums or len(nums)==1:
            return nums
        
        freq_dict = Counter(nums)
        
        most_frequent = []
        for key, value in freq_dict.items():
            most_frequent.append((value, key))
        
        most_frequent.sort(key=lambda val: val[0], reverse=True)
        
        return [most_frequent[i][1] for i in range(k)]
        