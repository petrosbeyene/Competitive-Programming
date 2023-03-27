class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        dic = Counter(words[0])

        for i in range(1, len(words)):
            cnt = Counter(words[i])
            for c, val in dic.items():
                if c in cnt and dic[c] == cnt[c]:
                    continue
                elif c in cnt:
                    dic[c] = min(dic[c], cnt[c])
                else:
                    dic[c] = 0
        
        ans = []
        for key, val in dic.items():
            if val != 0:
                ans.extend(val*[key])
        
        return ans

        #Time Complexity: O(n**2)
        #Space Complexity: O(n)
