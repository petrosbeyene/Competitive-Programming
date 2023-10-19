class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        # Here is the intution:
        # if min(nums) + k >= max(nums) - k:
        #   We can somehow make all the elements equal
        # but if min(nums) + k < max(nums) - k:
        #   Our best chance is going to be 
        #   (max(nums) - k) - (min(nums) + k)

        return max(0, ((max(nums)-k) - (min(nums)+k)))
