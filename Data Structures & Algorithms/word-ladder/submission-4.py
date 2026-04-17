class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def replaceChar(word, ind):
            wlist = list(word)
            wlist[ind] = '*'
            return ''.join(wlist)
        
        # Time O(NL^2), Space O(NL)
        adjlist = defaultdict(set)
        for w in wordList:
            for i in range(len(w)):
                wstar = replaceChar(w, i)
                adjlist[wstar].add(w)
        
        q = deque([beginWord])
        res = 0
        visited = set([beginWord])
        while q:
            currlen = len(q)
            res += 1
            for i in range(currlen):
                curr = q.popleft()
                if curr == endWord:
                    return res
                for j in range(len(curr)):
                    currstar = replaceChar(curr, j)
                    for nb in adjlist[currstar]:
                        if nb not in visited:
                            visited.add(nb)
                            q.append(nb)
        
        return 0
