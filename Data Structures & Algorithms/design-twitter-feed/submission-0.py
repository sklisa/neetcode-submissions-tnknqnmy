class Twitter:

    def __init__(self):
        self.time = 0
        self.posts = defaultdict(list)   # user: list of tweets
        self.following = defaultdict(set)   # user: followee


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        self.following[userId].add(userId)
        for followee in self.following[userId]:
            for post in self.posts[followee]:
                heapq.heappush(heap, (post[0], post[1]))
                if len(heap) > 10:
                    heapq.heappop(heap)
        res = []
        for _ in range(min(len(heap), 10)):
            _, post = heapq.heappop(heap)
            res.append(post)
        res.reverse()
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
