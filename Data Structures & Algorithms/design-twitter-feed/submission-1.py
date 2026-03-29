class Twitter:

    def __init__(self):
        self.following = {}
        self.posts = deque()
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts.appendleft((userId, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []

        i = 0
        while i < len(self.posts) and len(res) != 10:
            user, tweetId = self.posts[i]
            if user == userId or (userId in self.following and user in self.following[userId]):
                res.append(tweetId)
            i += 1
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        try:
            self.following[followerId].remove(followeeId)
        except KeyError:
            pass
