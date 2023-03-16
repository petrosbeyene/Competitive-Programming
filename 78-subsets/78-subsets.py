class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(candidate, index):
            if index == len(nums):
                ans.append(candidate[:])
                return
            
            #Pick
            candidate.append(nums[index])
            backtrack(candidate, index + 1)

            #Don't Pick
            candidate.pop()
            backtrack(candidate, index + 1)
        
        backtrack([], 0)
        return ans

