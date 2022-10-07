class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [*range(1, n+1)]
        i = 0
        def circularGm(i, k):
            if len(players) == 1:
                return players[0]
            i = (i+k-1)%len(players)
            del players[i]
            return circularGm(i, k)
        
        return circularGm(i, k)
        