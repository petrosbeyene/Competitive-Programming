class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = []
        curr_max = -1
        for val in arr[::-1]:
            ans.append(curr_max)
            if val > curr_max:
                curr_max = val
        
        return ans[::-1]

        
