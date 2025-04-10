from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_map = defaultdict(list)
        for word in strs:
            curr = "".join(sorted(word))
            anagram_map[curr].append(word)
        
        return list(anagram_map.values())

        # Time complexity: O(n*mlogm), when n is the length of strs array, and m is the length of the longest string
        # Space complexity: O(n*m), same assumption as the above