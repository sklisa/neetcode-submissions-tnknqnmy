class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Time O(N^2)
        nums.sort()
        l, r = 0, len(nums)-1
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums)-1
            while l < r:
                curr = nums[i] + nums[l] + nums[r]
                if curr == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif curr < 0:
                    l += 1
                else:
                    r -= 1
        return res