class Solution:
    def smallerNumbersThanCurrent(self, nums):
        outPutArr = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    outPutArr[i] += 1
                
        return outPutArr
