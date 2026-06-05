class Twitter:

    def __init__(self):
        self.storage: dict[int, list[tuple[int, int]]] = {}
        self.following: dict[int, set[int]] = {}
        self.time = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.storage.setdefault(userId, []).append((self.time, tweetId))

    # optimized feed generation with k-way merge
    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        users = self.following.get(userId, set()) | {userId}
        for uid in users:
            tweets = self.storage.get(uid, [])
            if tweets:
                idx = len(tweets) - 1
                time, tweetId = tweets[idx]
                heapq.heappush(heap, (-time, tweetId, uid, idx))

        res = []
        while heap and len(res) < 10:
            _, tweetId, uid, idx = heapq.heappop(heap)
            res.append(tweetId)
            prev_idx = idx - 1
            if prev_idx >= 0:
                prev_time, prev_tweetId = self.storage[uid][prev_idx]
                heapq.heappush(heap, (-prev_time, prev_tweetId, uid, prev_idx))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following.setdefault(followerId, set()).add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)
        