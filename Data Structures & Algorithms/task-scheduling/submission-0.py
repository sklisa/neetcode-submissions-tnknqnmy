class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        heap = [] # (-remaining_freq)
        q = deque() # (available_time, -remaining_freq)
        for k, v in counter.items():
            heapq.heappush(heap, -1 * v)
        
        t = 0
        while heap or q:
            t += 1
            if heap:
                neg_cnt = heapq.heappop(heap)
                cnt = neg_cnt * -1
                cnt -= 1
                if cnt != 0:
                    q.append((t + n, -1 * cnt))
            
            if q and t == q[0][0]:
                _, neg_cnt = q.popleft()
                heapq.heappush(heap, neg_cnt)

        return t