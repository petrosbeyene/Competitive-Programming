class Solution:    
    def largestMerge(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        merged = ""
        while i < len(word1) and j < len(word2):
            if word1[i] > word2[j]:
                merged += word1[i]
                i += 1
            elif word2[j] > word1[i]:
                merged += word2[j]
                j += 1
            else:
                if word1[i:] > word2[j:]:
                    merged += word1[i]
                    i += 1
                else:
                    merged += word2[j]
                    j += 1
        
        if i < len(word1):
            merged += word1[i:]
        
        if j < len(word2):
            merged += word2[j:]
        
        return merged
