class Solution:
    def searchInsert(self, nums, target: int) -> int:
        beg = 0
        end = len(nums)-1
        while beg <= end:
            mid = beg + (end - beg)//2
            if nums[mid] == target:
                return mid
            elif nums[mid-1] <= target <=nums[mid] and target not in nums:
                return mid
            
            elif nums[mid] < target:
                beg = mid + 1
            else:
                end = mid - 1
        
        return len(nums) if nums[len(nums)-1] <= target else 0