class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [*range(1, n+1)]
        while len(players) > 1:
            i = (k-1)%len(players)
            players = players[i+1:] + players[:i]
        return players[0]
        
            
        
