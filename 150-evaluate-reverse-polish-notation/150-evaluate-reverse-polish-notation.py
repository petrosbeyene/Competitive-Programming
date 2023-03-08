class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in tokens:
            if i not in ["+", "-", "*", "/"]:
                stack.append(int(i))
            else:
                r_operand = stack.pop()
                l_operand = stack.pop()
                
                if i == '+':
                    stack.append(l_operand + r_operand)
                elif i == '-':
                    stack.append(l_operand - r_operand)
                elif i == '*':
                    stack.append(l_operand * r_operand)
                elif i == '/':
                    stack.append(int(l_operand / r_operand))
                    
        return stack.pop()
        
