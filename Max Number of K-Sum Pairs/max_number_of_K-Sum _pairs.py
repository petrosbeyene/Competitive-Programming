class Solution:
    def maxOperations(self, nums, k):
        frequency_dict = {}
        count = 0
 
        for i in nums :
            if ((i in frequency_dict) and frequency_dict[i] > 0):       
                frequency_dict[i] -= 1
                count += 1
            elif k - i in frequency_dict:
                frequency_dict[k - i] += 1
            else:
                frequency_dict[k - i] = 1
     
        return count