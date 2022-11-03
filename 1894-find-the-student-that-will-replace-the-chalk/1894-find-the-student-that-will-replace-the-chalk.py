class Solution:
    def chalkReplacer(self, chalk, k: int) -> int:
        for i in range(1, len(chalk)):
            chalk[i] += chalk[i-1]
        
        k %= chalk[-1]
        for i in range(len(chalk)):
            if chalk[i] < k:
                continue
            elif chalk[i] == k:
                return i+1
            else:
                return i