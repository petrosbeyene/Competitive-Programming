import heapq


class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        
        return nums[0]