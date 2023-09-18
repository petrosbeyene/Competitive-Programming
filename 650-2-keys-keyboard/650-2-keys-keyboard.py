class Solution:
    def minSteps(self, n: int) -> int:
        dp = [None]*(n+1)
        dp[0], dp[1] = 0, 0
        for i in range(2, n+1):
            for j in range(2, i):
                if i%j == 0:
                    dp[i] = dp[j] + dp[i//j]
            if dp[i] == None:
                dp[i] = i
        
        return dp[n]
        
