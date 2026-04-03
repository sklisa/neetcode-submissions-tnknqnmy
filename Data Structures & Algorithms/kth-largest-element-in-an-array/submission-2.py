class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # quick select
        # Time O(n) in average, O(n^2) worst case
        # Space O(n) for recursion stack
        def quickselect(l, r):
            p, pivot = l, nums[r]
            for i in range(l, r):
                if nums[i] > pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            
            if p == (k-1):
                return nums[p]
            elif p < (k-1):
                return quickselect(p+1, r)
            else:
                return quickselect(l, p-1)
        
        return quickselect(0, len(nums)-1)