class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Time O(N), Space O(1)
        l, r = 0, 0
        seen = defaultdict(int)
        res = 0
        while r < len(s):
            seen[s[r]] += 1
            while (r - l + 1 - max(seen.values())) > k: # condition being the non major chars exceeds k
                seen[s[l]] -= 1
                if seen[s[l]] == 0:
                    seen.pop(s[l])
                l += 1
            res = max(res, r-l+1)
            r += 1
        return res
