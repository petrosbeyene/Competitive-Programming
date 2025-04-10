class Solution:
    def findDifference(self, nums1, nums2):
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        ans = [[], []]

        for elem in nums1_set:
            if elem not in nums2_set:
                ans[0].append(elem)
        
        for elem in nums2_set:
            if elem not in nums1_set:
                ans[1].append(elem)
        
        return ans

        #Time Complexity: O(N + M)
        #Space Complexity: O(N + M)


        