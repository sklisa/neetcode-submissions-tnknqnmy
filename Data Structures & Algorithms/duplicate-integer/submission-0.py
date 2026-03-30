class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appeared = set()
        for i in nums:
            if i in appeared:
                return True
            else:
                appeared.add(i)
        return False

        