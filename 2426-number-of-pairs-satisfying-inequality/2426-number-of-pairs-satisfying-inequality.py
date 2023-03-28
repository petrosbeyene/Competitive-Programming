class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        ## The First Trick to do this question is:
        ## to rearrange the equation provided on the question to -
        ## nums1[i] - nums2[i] <= nums1[j] - nums2[j] + diff
        ## This will let us have a merged array of difference.
        def findCorrectPlace(target, arr, low, high):
            if high >= low:
                mid = low + (high - low)//2

                if arr[mid] <= target:
                    return findCorrectPlace(target, arr, mid+1, high)
                else:
                    return findCorrectPlace(target, arr, low, mid-1)
            
            return low

          
        merged = [(nums1[i]-nums2[i]) for i in range(len(nums1))]
        
        ## Now Do Merge Sort on the merged array:
        count = 0
        def mergeSort(arr, diff):
            nonlocal count
            if len(arr) > 1:
                mid = len(arr)//2
                right = arr[mid:]
                left = arr[:mid]

                mergeSort(right, diff)
                mergeSort(left, diff)

                for n in right:
                    count += findCorrectPlace(n+diff, left, 0, len(left)-1)

                i = j = k = 0
                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        arr[k] = left[i]
                        i += 1
                    else:
                        arr[k] = right[j]
                        j += 1
                    k += 1
                
                while i < len(left):
                    arr[k] = left[i]
                    i += 1
                    k += 1
                
                while j < len(right):
                    arr[k] = right[j]
                    j += 1
                    k += 1
        

        mergeSort(merged, diff)
        return count

        ## Time Complexity: O(2*nlog n)
        ## Space Complexity: O(n)



