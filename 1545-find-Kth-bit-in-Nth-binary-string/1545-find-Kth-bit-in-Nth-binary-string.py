class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def recur(n, k):
            if n == 1:
                return 0
            mid = (2**n)//2
            if k == mid:
                return 1
            elif k > mid:
                return 1 - int(self.findKthBit(n-1, mid*2-k))
            else:
                return self.findKthBit(n-1, k)
        
        return str(recur(n, k))
