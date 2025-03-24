class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char == ']':
                curr_str = ''
                curr_k = ''
                while stack and stack[-1] != '[':
                    curr_str = stack.pop() + curr_str
                
                stack.pop()

                while stack and stack[-1].isdigit():
                    curr_k = stack.pop() + curr_k

                curr_str = curr_str * int(curr_k)
                stack.append(curr_str)
            else:
                stack.append(char)
        
        return ''.join(stack)

        # Time complexity: O(N)
        # Space complexity: O(N)