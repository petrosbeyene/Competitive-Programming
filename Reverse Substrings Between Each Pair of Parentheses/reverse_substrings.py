class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        size = len(s)
        for i in range(size):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                replaced = s[stack[-1]: i+1]
                s = s[:stack[-1]] + replaced[::-1] + s[i+1:]
                del stack[-1]
        
        ans = ''
        for i in s:
            if i != '(' and i != ')':
                ans += i
        return ans
                
                
                