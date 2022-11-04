from collections import Counter


class Solution:
    def minSetSize(self, arr) -> int:
        freq_dict = Counter(arr)
        
        freq_list = sorted(freq_dict.values(), reverse=True)
        
        i = 0
        half = len(arr)/2
        while half > 0:
            half -= freq_list[i]
            i += 1
        
        return i