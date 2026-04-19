class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums)-1
        while l < r:
            if l == r-1:
                return min(nums[l], nums[r])
            mid = (l+r) // 2
            if nums[mid] < nums[r] < nums[l]:
                r = mid
            elif nums[r] < nums[l] < nums[mid]:
                l = mid
            else:
                return nums[l]
        return nums[l]