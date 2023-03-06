class Solution:
    def searchRange(self, nums, target: int):
        ans = [-1, -1]
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] == target:
                ans[0] = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] == target:
                ans[1] = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        
        return ans
