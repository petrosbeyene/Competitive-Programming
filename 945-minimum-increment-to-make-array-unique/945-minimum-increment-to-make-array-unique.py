from collections import Counter


class Solution:
    def minIncrementForUnique(self, nums) -> int:
        count = Counter(nums)
        duplicates = []
        max_val = max(nums)
        moves = 0
        for n in range(len(nums)+ max_val):
            if count[n] >= 2:
                duplicates.extend([n]*(count[n]-1))
            else:
                if duplicates and count[n] == 0:
                    moves += (n-duplicates.pop())
        return moves