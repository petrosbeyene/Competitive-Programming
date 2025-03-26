class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        final_str = ''
        while i < len(word1) and j < len(word2):
            final_str += word1[i] 
            final_str += word2[j]
            i += 1
            j += 1
        
        if i < len(word1):
            final_str += word1[i:]
        
        elif j < len(word2):
            final_str += word2[j:]
        
        return final_str

        # Time complexity: O(N), where N is the maximum length of word1 and word2.
        # Space complexity: O(N + M) in the general case due to string concatenation.
        # However, given the problem constraints (1 ≤ len(word1), len(word2) ≤ 100), 
        # the space complexity can be considered O(1) in practice.