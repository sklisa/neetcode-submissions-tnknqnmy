class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mins = []
        maxs = []
        temp = prices[0]
        for i in range(len(prices)):
            temp = min(temp, prices[i])
            mins.append(temp)
        temp = prices[-1]
        for i in range(len(prices)-1, -1, -1):
            temp = max(temp, prices[i])
            maxs.append(temp)
        maxs.reverse()

        res = 0
        for i in range(len(prices)):
            res = max(res, maxs[i] - mins[i])
        return res