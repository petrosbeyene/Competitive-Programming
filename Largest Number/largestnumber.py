class Solution:
    def largestNumber(self, nums):
        nums_str = list(map(str, nums))
        
        for i in range(len(nums_str)):
            for j in range(i, len(nums_str)):
                choice_1 = int(nums_str[i]+nums_str[j])
                choice_2 = int(nums_str[j]+nums_str[i])
                if choice_2 > choice_1:
                    nums_str[i], nums_str[j] = nums_str[j], nums_str[i]
                else:
                    continue
        
        final = ''.join(nums_str)
        return '0' if final[0] == '0' else final
