class Solution:
    def backtrack(self, candidate, ans, curr, n, k):
        if len(candidate)==k:
            ans.append(candidate[:])
            return
        
        if curr > n:
            return
        
        for i in range(curr, n+1):
            candidate.append(i)
            self.backtrack(candidate, ans, i+1, n, k)
            candidate.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        self.backtrack([], ans, 1, n, k)

        return ans
