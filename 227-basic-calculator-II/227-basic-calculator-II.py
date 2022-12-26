class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        i = 0
        s = s.replace(' ', '')
        operators = ['+']

        if not s:
            return 0

        while i < len(s):
            if s[i].isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                curr_num = int(s[start:i])

                if operators and operators[-1] in '*/-':
                    operator = operators.pop()
                    if operator == '-':
                        curr_num = -1 * curr_num
                    else:
                        prev_val = stack.pop()
                        curr_num = int(prev_val/curr_num) if operator=='/' else prev_val * curr_num
                
                stack.append(curr_num)
            elif s[i] in '+-*/':
                operators.append(s[i])
                i += 1
            else:
                i += 1
        
        return stack[0] if len(stack)==1 else sum(stack)