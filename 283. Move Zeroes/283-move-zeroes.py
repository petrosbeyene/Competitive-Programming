class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = trav = 0
        while trav < len(nums):
            if nums[trav] != 0:
                nums[start], nums[trav] = nums[trav], nums[start]
                start += 1
            trav += 1
        