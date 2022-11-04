class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):
        ans = [True]*len(l)
        for i in range(len(l)):
            temp = nums[l[i]:r[i]+1]
            temp.sort()
            val = temp[1] - temp[0]
            
            j, k = 1, 2
            while k < len(temp):
                if temp[k] - temp[j] != val:
                    ans[i] = False
                j += 1
                k += 1
            
        return ans  