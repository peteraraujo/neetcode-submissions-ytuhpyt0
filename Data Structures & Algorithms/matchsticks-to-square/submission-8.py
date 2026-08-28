from heapq import heapify, heappop, heappush

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        size = len(matchsticks)
        total = sum(matchsticks)
        maxMatchAllowed = total / 4
        maxMatch = max(matchsticks)

        if size < 4 or total % 4 != 0 or maxMatch > maxMatchAllowed:
            return False
        
        buckets = [0, 0, 0, 0]
        matchsticks.sort(reverse=True)

        def dfs(i=0):

            if i == size:
                n = buckets[0]

                for bi in range(1, 4):
                    if buckets[bi] != n:
                        return False
                
                return True
            
            for bi in range(4):
                buckets[bi] += matchsticks[i]
                if buckets[bi] > maxMatchAllowed:
                    buckets[bi] -= matchsticks[i]
                    continue
                if dfs(i + 1):
                    return True
                buckets[bi] -= matchsticks[i]
            
            return False
        
        return dfs()

            