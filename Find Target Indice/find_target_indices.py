class Solution:
    def targetIndices(self, nums, target):
        n = len(nums)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
        output = []   
        for i in range(n):
            if nums[i] == target:
                output.append(i)
        return output
                
        