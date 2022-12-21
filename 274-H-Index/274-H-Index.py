class Solution:
    def hIndex(self, citations) -> int:
        citations.sort( reverse = True )
        
        for idx, citation in enumerate(citations):
           if idx >= citation:
                return idx
        
        return len(citations)