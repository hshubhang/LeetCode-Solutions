class Twitter:

    def __init__(self):
        
        self.tweet_history = defaultdict(list)
        self.follow_map = defaultdict(set)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweet_history[userId].append((self.time, tweetId))
       

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        heapq.heapify(minHeap)
        #get user tweets first
        for tweet in self.tweet_history[userId]:
            heapq.heappush(minHeap, tweet)
            if minHeap and len(minHeap) > 10:
                heapq.heappop(minHeap)
                
        #get tweets of all the followers that user follows
        followlist = self.follow_map[userId]
        for followid in followlist:
            for tweet in self.tweet_history[followid]:
                heapq.heappush(minHeap, tweet)
                if minHeap and len(minHeap) > 10:
                    heapq.heappop(minHeap)

        tweets = list(minHeap)
        tweets.sort(reverse=True)
        feed = [tweetId for _, tweetId in tweets]
        return feed
            
        
    def follow(self, followerId: int, followeeId: int) -> None:
        #add the follower as the key as people following as value
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        #remove the followee from the follower list
        self.follow_map[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)