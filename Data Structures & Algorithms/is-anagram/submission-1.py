class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Space O(n), Time O(n)
        if len(s) != len(t):
            return False
        
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for i in s:
            s_dict[i] += 1
        
        for j in t:
            t_dict[j] += 1

        for k, v in s_dict.items():
            if t_dict[k] != v:
                return False

        return True