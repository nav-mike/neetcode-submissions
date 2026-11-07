from functools import partial

class Twitter:

    def __init__(self):
        self.count = 0
        self.users = defaultdict(set)
        self.posts = defaultdict(partial(deque, maxlen=10))
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append([self.count, tweetId])
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        min_heap = []

        sources = self.users[userId] | {userId}
        if len(sources) > 10:
            max_heap = []
            for fid in sources:
                index = len(self.posts[fid]) - 1
                if index >= 0:
                    count, tweetId = self.posts[fid][index]
                    heapq.heappush(max_heap, [-count, tweetId, fid, index-1])

                    if len(min_heap) > 10:
                        heapq.heappop(max_heap)
            
            while max_heap:
                count, tweetId, fid, index = heapq.heappop(max_heap)
                heapq.heappush(min_heap, [-count, tweetId, fid, index])
            
        else:
            for fid in sources:
                index = len(self.posts[fid]) - 1
                if index >= 0:
                    count, tweetId = self.posts[fid][index]
                    heapq.heappush(min_heap, [count, tweetId, fid, index-1])
        
        while min_heap and len(result) < 10:
            _, tweetId, fid, index = heapq.heappop(min_heap)
            result.append(tweetId)

            if index >= 0:
                count, tweetId = self.posts[fid][index]
                heapq.heappush(min_heap, [count, tweetId, fid, index-1])

        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users:
            self.users[followerId].discard(followeeId)
        
