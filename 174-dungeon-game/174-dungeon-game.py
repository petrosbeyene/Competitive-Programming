class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])
        dp = [[float("-inf") for _ in range(m+1)] for _ in range(n+1)]
        
        dp[n][m-1] = 0
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                dp[i][j] = dungeon[i][j] + max(dp[i+1][j], dp[i][j+1])
                
                if dp[i][j] > 0:
                    dp[i][j] = 0
                    
        return abs(dp[0][0]) + 1
