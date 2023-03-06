class Solution:
    def peakIndexInMountainArray(self, arr) -> int:
        low, high = 0, len(arr)-1
        while low <= high:
            mid = low + (high - low)//2
            if arr[mid] >= arr[mid+1]:
                high = mid -1
            else:
                low = mid + 1
        
        return low

        ## time complexity: O(log n)
        ## space complexity: O(1)