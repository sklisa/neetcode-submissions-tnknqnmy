class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Time O(mn), Space O(mn)
        result = defaultdict(list)
        for s in strs:
            character = [0] * 26
            for c in s:
                character[ord(c) - ord('a')] += 1
            result[tuple(character)].append(s)

        return list(result.values())