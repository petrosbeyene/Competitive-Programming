class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(left, right):
            if left > right:
                return
            s[right], s[left] = s[left], s[right]
            return reverse(left+1, right-1)
        
        reverse(0, len(s)-1)
