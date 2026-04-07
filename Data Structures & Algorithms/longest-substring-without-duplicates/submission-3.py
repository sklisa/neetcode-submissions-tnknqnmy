class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        seen = set()
        l, r = 0, 0
        res = 0
        for r in range(len(s)):
            while l < r and s[r] in seen:
                res = max(res, r-l)
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
        res = max(res, r-l+1)
        return res