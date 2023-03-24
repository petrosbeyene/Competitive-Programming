class Solution:
    def quickSort(self, arr, left, right):
        if left < right:
            pivotIdx = self.findPivot(arr, left, right)
            self.quickSort(arr, pivotIdx+1, right)
            self.quickSort(arr, left, pivotIdx-1)
    
    def findPivot(self, arr, left, right):
        currIdx = left - 1
        pivotIdx = right
        for i in range(currIdx+1, right+1):
            if arr[i] < arr[pivotIdx]:
                currIdx += 1
                arr[i], arr[currIdx] = arr[currIdx], arr[i]
        
        arr[currIdx+1], arr[i] = arr[i], arr[currIdx+1]
        return currIdx + 1

    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.quickSort(nums, 0, len(nums)-1)
        j = len(nums)-k
        return nums[j]
        
