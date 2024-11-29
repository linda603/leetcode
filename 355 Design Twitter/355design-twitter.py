class Twitter:

    def __init__(self):
        self.followee = defaultdict(set)
        self.tweet = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        self.followee[userId].add(userId)
        for followeeId in self.followee[userId]:
            if followeeId in self.tweet:
                idx = len(self.tweet[followeeId]) - 1
                cnt, tweetId = self.tweet[followeeId][idx]
                heap.append([cnt, tweetId, followeeId, idx - 1]) # push tweetId and next idx if we take tweet from followeeId next time
        heapq.heapify(heap)
        
        while heap and len(res) < 10:
            cnt, tweetId, followeeId, idx = heapq.heappop(heap)
            res.append(tweetId)
            if idx >= 0:
                cnt, tweetId = self.tweet[followeeId][idx]
                heapq.heappush(heap, [cnt, tweetId, followeeId, idx - 1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followee[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followee[followerId]:
            self.followee[followerId].remove(followeeId)

# Time: getNewsFeed: O(k + logk + 10logk) = (k). k: number of followees that userId followed
#       postTweet, follow, unfollow O(1)
# Space: O()

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)