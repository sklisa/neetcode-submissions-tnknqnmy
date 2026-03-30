class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = nums[0]
        for i in range(len(nums)):
            if farthest < i:
                return False
            farthest = max(farthest, nums[i] + i)
        return farthest >= len(nums) - 1