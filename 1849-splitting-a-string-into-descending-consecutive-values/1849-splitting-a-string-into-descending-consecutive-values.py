class Solution:
    def backtrack(self, idx, prev, s):
        if idx == len(s):
            return True

        for j in range(idx, len(s)):
            curr = int(s[idx:j+1])
            if prev == curr + 1 and self.backtrack(j+1, curr, s):
                return True
        return False


    def splitString(self, s: str) -> bool:
        for i in range(len(s)-1):
            val = int(s[:i+1])
            if self.backtrack(i+1, val, s):
                return True
        
        return False
