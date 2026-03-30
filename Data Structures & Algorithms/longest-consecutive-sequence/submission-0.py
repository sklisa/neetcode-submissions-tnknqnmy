class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Time O(n), Space O(n)
        pos = defaultdict(int)
        res = 0
        for n in nums:
            if pos[n] == 0:
                pos[n] = pos[n-1] + pos[n+1] + 1
                pos[n - pos[n-1]] = pos[n]
                pos[n + pos[n+1]] = pos[n]
                res = max(res, pos[n])
        return res
