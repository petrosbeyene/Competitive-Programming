class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for ch in s:
            if not stack or stack[-1][0] != ch:
                stack.append([ch, 1])
            elif stack[-1][0] == ch:
                stack[-1][1] += 1
            
            if stack[-1][1] == k:
                stack.pop()
        
        ans = [stack[i][0] * stack[i][1] for i in range(len(stack))]
        return "".join(ans)

