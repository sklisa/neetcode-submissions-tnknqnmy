class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # monotonically increasing stack
        # when run into a lower bar, calculate the area the top bar can make to the right of it before reaching the lower bar
        # the left boundary for each bar is kept track in the stack
        # then add the lower bar to the stack so we can trace the largest rectangle to the right of it
        stack = [] # (height, startInd)
        res = 0
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][0] > heights[i]:
                tall, start = stack.pop()
                area = (i - start) * tall
                res = max(res, area)
            stack.append((heights[i], start))

        for h in stack:
            area = (len(heights) - h[1]) * h[0]
            res = max(res, area)

        return res