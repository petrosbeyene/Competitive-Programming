class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # define the objective function
        # f(i, j) = the number of possible unique paths 
        #           that the robot can take to reach the bottom-right corner.
        
        # base cases
        # f(0, 0) = 1

        # Transition function
        # f(i, j) = f(i-1, j) + f(i, j-1)

        dp = [[None]*(n)]*(m)
        dp[0][0] = 1
        ##Even Better Implementation
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                elif i > 0:
                    dp[i][j] = dp[i-1][j]
                elif j > 0:
                    dp[i][j] = dp[i][j-1]
        
        return dp[m-1][n-1]
