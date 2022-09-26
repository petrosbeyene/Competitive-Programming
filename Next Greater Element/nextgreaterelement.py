class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        a_dict ={}
        for i in range(len(nums2)):
            a_dict[nums2[i]] = -1
        
        for i in range(len(nums2)):
            while len(stack) > 0 and nums2[i] > stack[-1]:
                val = stack.pop()
                a_dict[val] = nums2[i]
            stack.append(nums2[i])
        
        for i in range(len(nums1)):
            nums1[i] = a_dict[nums1[i]]
        
        return nums1