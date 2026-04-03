class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # monotonically increasing stack
        # two pass to find the left and right boundary respectively
        stack = [] # (height, startInd)
        left = []
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][0] >= heights[i]:
                tall, start = stack.pop()
            stack.append((heights[i], start))
            left.append(start)
        
        stack = []
        right = []
        for i in range(len(heights)-1, -1, -1):
            end = i
            while stack and stack[-1][0] >= heights[i]:
                tall, end = stack.pop()
            stack.append((heights[i], end))
            right.append(end)
        right.reverse()

        res = 0
        for i in range(len(heights)):
            area = (right[i] - left[i] + 1) * heights[i]
            res = max(res, area)

        return res