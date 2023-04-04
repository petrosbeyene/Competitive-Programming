class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        cnt = 0
        n = len(nums)
        for i in range(n):
            curr_gcd = 0
            for j in range(i, n):
                curr_gcd = gcd(curr_gcd, nums[j])

                #increment cnt if curr_gcd == k
                cnt += (curr_gcd == k)
        
        return cnt

