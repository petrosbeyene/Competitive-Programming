class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = set()
        
        def backtrack(curr, idx, l_val):
            if len(curr) >= 2 and tuple(curr) not in visited:
                ans.append(curr[:])
                visited.add(tuple(curr[:]))
            
            if idx == len(nums):
                return
            
            if nums[idx] >= l_val:
                # pick the number
                curr.append(nums[idx])
                backtrack(curr, idx+1, curr[-1])
                curr.pop()
                
                # don't pick the number
                backtrack(curr, idx+1, l_val)
                
            else:
                # skip the number
                backtrack(curr, idx+1, l_val)
                
        backtrack([], 0, float('-inf'))
        return ans
