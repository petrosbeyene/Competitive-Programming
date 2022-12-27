class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                sub_string = ""
                while stack[-1] != '[':
                    sub_string = stack.pop()+sub_string
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop()+k
                
                stack.append(int(k)*sub_string)
        
        return "".join(stack)