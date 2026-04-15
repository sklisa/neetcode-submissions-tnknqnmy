class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Time O(N), Space O(N)
        visited = set(i for i in range(numCourses))
        toCourse = defaultdict(set) # prereq: courses
        frCourse = defaultdict(set) # course: prereqs
        for to, fr in prerequisites:
            toCourse[fr].add(to)
            frCourse[to].add(fr)
            visited.discard(to)
        q = deque(list(visited)) # start with the courses without a prereq
        while q:
            curr = q.popleft()
            for nb in toCourse[curr]:
                frCourse[nb].discard(curr)
                if nb not in visited and len(frCourse[nb]) == 0:
                    visited.add(nb)
                    q.append(nb)
        
        return len(visited) == numCourses
