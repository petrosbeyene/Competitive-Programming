class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        satisfaction.sort()
        @cache
        def dp(currIdx, timeTaken):

            if currIdx == len(satisfaction):
                return 0
            
            val1 = timeTaken*satisfaction[currIdx] + dp(currIdx + 1, timeTaken + 1)  # Pick
            val2 = dp(currIdx + 1, timeTaken)  # Don't Pick

            return max(val1, val2)
        
        return dp(0, 1)
