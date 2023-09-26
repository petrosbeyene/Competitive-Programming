class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        i = 0
        age_score = [(0,0)]
        while i < len(scores):
            age_score.append((ages[i], scores[i]))
            i += 1
        
        age_score.sort()
        dp = [0]*(len(scores)+1)

        for i in range(1, len(scores)+1):
            max_score = age_score[i][1]
            for j in range(i-1, -1, -1):
                if age_score[i][1] >= age_score[j][1]:
                    max_score = max(max_score, age_score[i][1] + dp[j])    
            dp[i] = max_score

        return max(dp)
        
