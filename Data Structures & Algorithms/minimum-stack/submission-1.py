class Solution:
    def isValid(self, s: str) -> bool:
        pair = {')':'(', '}':'{', ']':'['}
        stack = []

        for c in s:
            if c in pair:
                if len(stack) == 0:
                    return False
                if stack[-1] == pair[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0
