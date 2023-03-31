class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ans = []
        for idx, n in enumerate(nums):
            if n == target:
                ans.append(idx)
        
        return ans
