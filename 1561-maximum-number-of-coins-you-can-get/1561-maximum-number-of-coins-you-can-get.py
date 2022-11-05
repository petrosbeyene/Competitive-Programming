class Solution:
    def maxCoins(self, piles) -> int:
        piles.sort()
        return sum(piles[len(piles)//3::2])