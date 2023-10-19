class Solution:
    def countPrimes(self, n: int) -> int:
        # Sieve of Eratosthenes
        primes = [True for _ in range(n+1)]

        p = 2
        while p * p <= n:

            if primes[p] == True:
                for e in range(p*p, n+1, p):
                    primes[e] = False

            p += 1
        

        ans = 0
        for i in range(2, n):
            if primes[i]:
                ans += 1
        
        return ans
