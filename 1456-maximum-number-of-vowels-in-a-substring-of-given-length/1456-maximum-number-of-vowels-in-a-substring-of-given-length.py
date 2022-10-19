from collections import defaultdict


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        d = defaultdict(int)
        d['a'] = d['e'] = d['i'] = d['o'] = d['u'] = 1
        
        begin = 0
        end = k -1
        
        count = 0
        for i in range(begin, end+1):
                count += d[s[i]]
        max_val = count
        
        while True:
            begin += 1
            end += 1
            if end < len(s):
                count += d[s[end]] - d[s[begin-1]]
                max_val = max(max_val, count)
            
            if end >= len(s):
                break
        
        return max_val