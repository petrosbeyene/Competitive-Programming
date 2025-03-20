class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}

        for token in tokens:
            if token in operators:
                val2, val1 = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(val1 + val2)
                elif token == '-':
                    stack.append(val1 - val2)
                elif token == '*':
                    stack.append(val1 * val2)
                else:
                    stack.append(int(val1 / val2))
            
            else:
                stack.append(int(token))

        return stack[0]
