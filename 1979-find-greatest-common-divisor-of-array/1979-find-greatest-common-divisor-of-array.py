class Solution:
    def calcGcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.calcGcd(b, a%b)
    
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        return self.calcGcd(nums[0], nums[-1])
