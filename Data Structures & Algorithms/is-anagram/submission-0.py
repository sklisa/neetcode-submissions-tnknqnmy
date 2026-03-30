class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Space O(n), Time O(nlogn)
        if len(s) != len(t):
            return False
        
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        return sorted_s == sorted_t