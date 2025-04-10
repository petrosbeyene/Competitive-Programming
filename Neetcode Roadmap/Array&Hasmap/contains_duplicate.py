from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
    
    # Time Complexity: O(N)
    # Space Complexity: O(N)