class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        size = len(coins)

        cache = {} # (current, start) : combinations

        def dfs(current=0, start=0):
            
            query = (current, start)

            if current > amount:
                return 0

            if current == amount:
                return 1
            
            if query in cache:
                return cache[query]
            
            totalCbs = 0

            for i in range(size - 1, start - 1, -1):
                
                cbs = dfs(current + coins[i], i)

                totalCbs += cbs

                cache[current, i] = totalCbs

            return totalCbs
        
        res = dfs()
        return res






            
        

        