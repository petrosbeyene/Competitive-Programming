class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        arr = matrix[0]
        ans = [[val] for val in arr]
        for i in range(1, len(matrix)):
            curr = matrix[i]
            for j in range(len(curr)):
                ans[j].append(curr[j])
        
        return ans
