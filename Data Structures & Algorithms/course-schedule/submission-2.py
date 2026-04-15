class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Time O(N), Space O(N)
        toCourse = defaultdict(set) # prereq: courses
        frCourse = [0] * numCourses
        for to, fr in prerequisites:
            toCourse[fr].add(to)
            frCourse[to] += 1
        
        q = deque() # start with the courses without a prereq
        for i in range(numCourses):
            if frCourse[i] == 0:
                q.append(i)
        
        finished = 0
        while q:
            curr = q.popleft()
            finished += 1
            for nb in toCourse[curr]:
                frCourse[nb] -= 1
                if frCourse[nb] == 0:
                    q.append(nb)
        
        return finished == numCourses
