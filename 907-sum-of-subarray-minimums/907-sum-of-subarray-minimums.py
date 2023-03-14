class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        ans = 0
        arr.append(float(-inf))
        for i, val in enumerate(arr):
            while stack and val < stack[-1][1]:
                cur_idx, cur_val = stack.pop()
                l_bound = -1 if not stack else stack[-1][0]
                pos_subarrays = (i-cur_idx)*(cur_idx-l_bound)
                ans += (cur_val)*pos_subarrays
            
            stack.append((i,val))
        
        return (ans%(10**9+7))
