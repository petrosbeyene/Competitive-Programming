class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return (2**(n).bit_length())-1 == n ^ (n>>1)
