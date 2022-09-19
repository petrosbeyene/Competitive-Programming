class Solution:
    def kthLargestNumber(self, nums, k: int) -> str:
        nums.sort(key=lambda num:int(num),reverse=True)
        return nums[k-1]