class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        size = len(coins)

        cache = {} # (i, current) = cbs

        def dfs(i=0, current=0):

            query = (i, current)

            if i == size or current > amount:
                return 0

            if query in cache:
                return cache[query]
            
            if current == amount:
                return 1
            
            take = dfs(i, current + coins[i])
            skip = dfs(i + 1, current)

            total = take + skip

            cache[query] = total

            return take + skip
        
        return dfs()