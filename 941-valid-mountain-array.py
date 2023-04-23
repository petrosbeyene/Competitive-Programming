class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        idx = arr.index(max(arr))
        if idx == 0 or idx == len(arr)-1:
            return False

        arr1 = arr[:idx+1]
        arr2 = arr[idx:]

        for i in range(len(arr1)-1):
            if arr1[i] >= arr1[i+1]:
                return False
        for i in range(len(arr2)-1):
            if arr2[i] <= arr2[i+1]:
                return False
        
        return True
