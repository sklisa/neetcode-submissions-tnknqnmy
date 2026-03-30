class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # default is min heap
        # Time O(logn), Space O(n)
        pq = []
        freq = defaultdict(int)
        res = []

        for n in nums:
            freq[n] += 1
        
        for key, val in freq.items():
            heapq.heappush(pq, (-val, key))
        
        for i in range(k):
            _, num = heapq.heappop(pq)
            res.append(num)
        
        return res