class Solution:
    def numTeams(self, rating: List[int]) -> int:
        greater = [0] * len(rating)
        less = [0] * len(rating) 

        for i in range(len(rating)):
            for j in range(i+1, len(rating)):
                if rating[j] > rating[i]:
                    greater[i] += 1
                else:
                    less[i] += 1
        
        no_of_teams = 0
        for i in range(len(rating)-2):
            for j in range(i+1, len(rating)-1):
                if rating[i] < rating[j]:
                    no_of_teams += greater[j]
                else:
                    no_of_teams += less[j]
        
        return no_of_teams
