class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+', '-', '*', '/'])

        def runOperator(op, val1, val2):
            if op == '+':
                return val1 + val2
            elif op == '-':
                return val1 - val2
            elif op == '*':
                return val1 * val2
            else: # /
                if (val1 > 0 and val2 > 0) or (val1 < 0 and val2 < 0):
                    return math.floor(val1 / val2)
                else:
                    return math.ceil(val1 / val2)

        for t in tokens:
            if t in operators:
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(runOperator(t, operand1, operand2))
            else:
                stack.append(int(t))
            print(stack)
        
        return stack[-1]