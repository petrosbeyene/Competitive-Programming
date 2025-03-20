class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses_map = {'(':')', '{':'}', '[':']'}
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                if len(stack) != 0:
                    curr = stack.pop()
                    if parentheses_map[curr] != char:
                        return False
                else:
                    return False
                
        return len(stack)==0

        #Time complexity: O(N)
        #Space complexity: O(N)
