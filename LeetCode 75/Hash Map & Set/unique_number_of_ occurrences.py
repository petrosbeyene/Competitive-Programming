from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr_cntr = Counter(arr)
        values = list(arr_cntr.values())

        return len(set(values)) == len(values)

        # Time Complexity: O(N)
        # Space Complexity: O(N)