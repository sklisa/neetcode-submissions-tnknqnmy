class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Time O(ST), Space O(T)
        resl, resr = 0, -1
        counter = Counter(t)
        l, r = 0, 0
        while r < len(s):
            if s[r] in counter:
                counter[s[r]] -= 1
            while sum(v <= 0 for v in counter.values()) == len(counter):
                # record result
                if resr == -1:
                    resl, resr = l, r
                elif r - l < resr - resl:
                    resl, resr = l, r
                
                if s[l] in counter:
                    counter[s[l]] += 1
                l += 1
            r += 1
        if resr == -1:
            return ""
        return s[resl:resr+1]
