class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def invert(s):
            ans = []
            for i in range(len(s)):
                if s[i] == "1":
                    ans.append("0")
                else:
                    ans.append("1")
            return "".join(ans)
        
        def recur(n):
            if n == 1:
                return "0"
            prev = recur(n-1)
            return prev + "1" + invert(prev)[::-1]
        
        return recur(n)[k-1]
