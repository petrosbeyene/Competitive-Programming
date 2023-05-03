class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt_dict = Counter(nums)
        for key, val in cnt_dict.items():
            if val == 1:
                return key
