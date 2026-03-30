class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += '#'
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        str_list = []
        l, r = 0, 0
        while l < len(s) and r < len(s):
            while s[r] != '#':
                r += 1  # r points to #
            length = int(s[l:r])
            str_list.append(s[r + 1:r + 1 + length])
            l, r = r + 1 + length, r + 1 + length
        
        return str_list
