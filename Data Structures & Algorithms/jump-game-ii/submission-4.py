class Solution:
    def jump(self, nums: List[int]) -> int:
        # BFS
        # Time O(N), Space O(1)
        l, r = 0, 0
        farthest = 0
        step = 0

        while r < len(nums) - 1:
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            step += 1

        return step        
