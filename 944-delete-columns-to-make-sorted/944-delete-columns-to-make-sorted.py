class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        i = 0
        cnt = 0
        while i < len(strs[0]):
            temp = [s[i] for s in strs]
            if temp != sorted(temp):
                cnt += 1
            i += 1
        
        return cnt
