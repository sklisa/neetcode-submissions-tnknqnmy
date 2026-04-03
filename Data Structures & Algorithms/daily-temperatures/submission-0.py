class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [(temperatures[0], 0)] # (temp, index)
        for i in range(len(temperatures)):
            curr = temperatures[i]
            # pop when a warmer temp is found
            while len(stack) > 0:
                if curr > stack[-1][0]:
                    _, ind = stack.pop()
                    res[ind] = i - ind
                else:
                    break
            stack.append((curr, i))
        return res    
            