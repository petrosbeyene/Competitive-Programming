class Solution:
    def partitionLabels(self, s: str):
        rightMostdict = {l:idx for idx,l in enumerate(s)}
        
        right = 0
        left = 0
        res = []
        for i, letter in enumerate(s):
            right = max(right, rightMostdict[letter])
            
            if i == right:
                res.append(right-left+1)
                left = right + 1
        
        return res
        