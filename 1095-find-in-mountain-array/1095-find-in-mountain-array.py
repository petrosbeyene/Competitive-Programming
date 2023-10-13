# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        n = mountain_arr.length()

        # Find the position of the peak element
        l, r = 1, n-2 # We can disregard the edge elements as they can't be the peak element
        while l <= r:
            m = l + (r-l)//2

            left, mid, right = mountain_arr.get(m-1), mountain_arr.get(m), mountain_arr.get(m+1)
            if left < mid < right:
                l = m + 1
            elif left > mid > right:
                r = m - 1
            else:
                # left < mid > right
                break
        
        peak = m

        # Now we will do binary search in the both the strictly increasing
        # and strictly decreasing parts of the mountain array

        # Strictly increasing part
        l, r = 0, peak
        while l <= r:

            m = l + (r - l)//2
            curr = mountain_arr.get(m)
            if curr == target:
                return m
            
            elif curr < target:
                l = m + 1
            else:
                r = m - 1
        
        # If not found on the strictly increasing part,
        # then we do a binary search in the Strictly decreasing part

        # Strictly decreasing part of the array
        l, r = peak, n - 1
        while l <= r:

            m = l + (r - l)//2
            curr = mountain_arr.get(m)
            if curr == target:
                return m
            
            elif target > curr:
                r = m - 1
            else:
                l = m + 1
        
        return -1 
        
