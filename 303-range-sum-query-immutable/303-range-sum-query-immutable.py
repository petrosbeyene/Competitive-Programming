class NumArray:

    def __init__(self, nums: List[int]):
        self.numArray = nums
        
        self.prefSum = [0]*len(nums)
        self.prefSum[0] = nums[0]
        
        for i in range(1, len(self.prefSum)):
            self.prefSum[i] = self.prefSum[i-1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefSum[right]
        
        return self.prefSum[right] - self.prefSum[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
