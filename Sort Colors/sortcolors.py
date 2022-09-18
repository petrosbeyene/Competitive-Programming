class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        arrSize = len(nums)
        countArr = [0] * 3
        tempArr = [0] * arrSize
        
        for i in range(arrSize):
            countArr[nums[i]] += 1
        for i in range(1, 3):
            countArr[i] += countArr[i-1]
        
        i = arrSize - 1
        while i >= 0:
            tempArr[countArr[nums[i]] - 1] = nums[i]
            countArr[nums[i]] -= 1
            i -= 1
        
        for i in range(arrSize):
            nums[i] = tempArr[i]