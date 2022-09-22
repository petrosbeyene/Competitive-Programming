class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        frequency = Counter(nums)
        filterd = [*set(nums)]
        count = 0
        for num in filterd:
            n = frequency[num]
            count += (n*(n-1)//2)
        return count
        