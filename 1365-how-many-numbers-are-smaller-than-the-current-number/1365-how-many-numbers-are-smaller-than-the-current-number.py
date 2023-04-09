class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        
        sorted_pos = {}
        for idx, n in enumerate(sorted_nums):
            if n not in sorted_pos:
                sorted_pos[n] = idx
        

        ans = [0 for i in range(len(nums))]
        for idx, val in enumerate(nums):
            ans[idx] = sorted_pos[val]
        
        return ans
