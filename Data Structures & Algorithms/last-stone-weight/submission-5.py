import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = list(map(lambda x: -x, stones))
        heapq.heapify(stones)

        while len(stones) > 1:
            
            x, y = -heapq.heappop(stones), -heapq.heappop(stones)

            res = abs(x - y)
            if res > 0:
                heapq.heappush(stones, -res)
        
        if len(stones) > 0:
            return -stones[0]
        else:
            return 0

        return last