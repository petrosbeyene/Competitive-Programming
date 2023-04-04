class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            d = 2
            while d * d <= n:
                while n % d == 0:
                    s.add(d)
                    n //= d
                d += 1
            if n > 1:
                s.add(n)
            
        return len(s)
        
