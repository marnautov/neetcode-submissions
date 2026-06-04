class Twitter:

    def __init__(self):
        self.storage: dict[int, list[tuple[int, int]]] = {}
        self.following: dict[int, set[int]] = {}
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.storage.setdefault(userId, []).append((self.time, tweetId))

        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        users = self.following.get(userId, set()) | {userId}
        
        for uid in users:
            for time, tweetId in self.storage.get(uid, []):
                heapq.heappush(heap, (-time, tweetId))

        res = []
        while heap and len(res) < 10:
            _, tweetId = heapq.heappop(heap)
            res.append(tweetId)

        return res



        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following.setdefault(followerId, set()).add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)
        