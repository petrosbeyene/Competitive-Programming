class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.helper(x, -n)
        else:
            return self.helper(x, n)

    def helper(self, x, n):
        if n == 0:
            return 1

        temp = self.helper(x, n // 2)
        if n % 2 == 0:
            return temp * temp
        else:
            return temp * temp * x