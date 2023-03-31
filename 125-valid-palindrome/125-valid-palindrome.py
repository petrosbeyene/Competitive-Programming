class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()
        
        if not s:
            return True
        
        beg, end = 0, len(s)-1
        while beg <= end:
            if s[beg]==s[end]:
                pass
            else:
                return False
            beg += 1
            end -= 1
        
        return True
