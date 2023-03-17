class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(pos_sol, pos_sol_sum, index):
            if pos_sol_sum == target:
                ans.append(pos_sol[:])
                return
            
            if index == len(candidates) or target - pos_sol_sum < candidates[index]:
                return
            
            #We have two possible decision at every step
            #Pick Current Val
            pos_sol.append(candidates[index])
            backtrack(pos_sol, pos_sol_sum + candidates[index], index)

            #Don't Pick Current Val
            pos_sol.pop()
            backtrack(pos_sol, pos_sol_sum, index+1)
        
        candidates.sort()
        backtrack([], 0, 0)
        return ans
