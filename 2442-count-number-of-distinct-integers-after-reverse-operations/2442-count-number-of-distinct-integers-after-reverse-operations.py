class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        new_arr = []
        for n in nums:
            curr = str(n)
            curr = int(curr[::-1])
            new_arr.append(curr)
        
        nums += new_arr
        s = set(nums)
        return len(s)
