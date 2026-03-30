class Solution:
    def jump(self, nums: List[int]) -> int:
        # DP
        # Time O(), Space O(N)

        dp = [2**31] * len(nums)
        dp[-1] = 0 # last index

        for i in range(len(nums)-2, -1, -1): # right to left    
            # for each index, the step is, 1 + min of step of all reachable index
            right = min(len(nums), i + nums[i] + 1)
            for j in range(i, right):
                dp[i] = min(dp[i], dp[j] + 1)

        return dp[0]