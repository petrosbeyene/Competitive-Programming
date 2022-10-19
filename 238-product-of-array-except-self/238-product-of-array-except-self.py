class Solution:
    def productExceptSelf(self, nums):
        pref_prod = 1
        ans = []
        
        for num in nums:
            ans.append(pref_prod)
            pref_prod *= num
	
        # answer = leftProduct * rightProduct
        # here we are using reversed nums and ans
        suf_prod = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= suf_prod
            suf_prod *= nums[i]
        
        return ans
        