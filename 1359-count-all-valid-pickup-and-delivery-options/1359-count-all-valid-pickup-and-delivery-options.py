class Solution:
    def countOrders(self, n: int) -> int:
        dp_val = 1
        n *= 2
        while n > 0:
            valid_choices = n * (n - 1) // 2
            dp_val *= valid_choices
            n -= 2
        
        return dp_val % (10**9 + 7)
