class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        def dfs(i, combo, remain):
            if remain < 0:
                return
            
            if remain == 0:
                res.append(combo.copy())
                return

            for j in range(i, len(nums)):
                combo.append(nums[j])
                dfs(j, combo, remain - nums[j])
                combo.pop()

        
        dfs(0, [], target)
        return res