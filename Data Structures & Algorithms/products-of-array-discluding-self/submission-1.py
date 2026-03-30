class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Time O(n), Space O(n)
        res = []
        forward = [1]
        backward = [1]
        for i in range(len(nums)-1):
            forward.append(forward[-1] * nums[i])
            backward.append(backward[-1] * nums[len(nums)-i-1])
        
        backward.reverse()
        for i in range(len(nums)):
            res.append(forward[i] * backward[i])
        
        return res
            