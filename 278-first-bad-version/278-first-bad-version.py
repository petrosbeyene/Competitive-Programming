# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        beg, end = 0, n
        ans = n + 1
        while beg <= end:
            mid = (beg+end)//2
            if isBadVersion(mid):
                end = mid - 1
                ans = mid
            elif not isBadVersion(mid):
                beg = mid + 1
        return ans