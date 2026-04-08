class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Time O(S+T), Space O(T)
        resl, resr = 0, -1
        counter = Counter(t)
        window = defaultdict(int)
        have, need = 0, len(counter)  # distinct chars
        l, r = 0, 0
        while r < len(s):
            window[s[r]] += 1
            if window[s[r]] == counter[s[r]]:
                have += 1
            while have == need:
                if resr == -1:
                    resl, resr = l, r
                elif r - l < resr - resl:
                    resl, resr = l, r
                window[s[l]] -= 1
                if window[s[l]] < counter[s[l]]:
                    have -= 1
                l += 1
            r += 1
        if resr == -1:
            return ""
        return s[resl:resr+1]
