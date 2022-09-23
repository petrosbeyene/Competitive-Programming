class Solution:
    def isValid(self, s: str) -> bool:
        p_dict = { ')':'(', ']': '[', '}':'{' }
        stack = []
        for char in s:
            if char == '(' or char== '{' or char== '[':
                stack.append(char)
            else:
                if not stack:
                    return False
                elif p_dict[char] == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
        
        return True if len(stack)==0 else False
                    
        