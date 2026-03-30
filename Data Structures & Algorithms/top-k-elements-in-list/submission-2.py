class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # default is min heap
        # Time O(nlogk), Space O(n+k)
        pq = []
        freq = defaultdict(int)
        res = []

        for n in nums:
            freq[n] += 1
        
        for key, val in freq.items():
            heapq.heappush(pq, (val, key))
            if len(pq) > k:
                heapq.heappop(pq) # pop the min
        
        for i in range(k):
            _, num = heapq.heappop(pq)
            res.append(num)
        
        return res