class Solution:
    def jump(self, nums: List[int]) -> int:
        # BFS
        # Time O(N^2), Space O(N)
        q = deque()
        q.append(0) # index 0
        seen = set([0])
        step = 0

        while q:
            currlen = len(q)
            for _ in range(currlen):
                ind = q.popleft()
                if ind == len(nums)-1:
                    return step
                for i in range(ind+1, ind+nums[ind]+1):
                    if i not in seen:
                        q.append(i)
                        seen.add(i)
            step += 1
                    
