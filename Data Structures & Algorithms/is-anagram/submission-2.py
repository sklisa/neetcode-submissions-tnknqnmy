class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Space O(1), Time O(n)
        if len(s) != len(t):
            return False
        
        characters = [0] * 26

        for i in range(len(s)):
            characters[ord(s[i])-ord('a')] += 1
            characters[ord(t[i])-ord('a')] -= 1
        
        for j in characters:
            if j != 0:
                return False

        return True