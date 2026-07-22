class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        size = len(stones)

        total = sum(stones)
        target = total // 2

        cache = {} # (i, current) : result

        def dfs(i=0, current=0):
            query = (i, current)

            if query in cache:
                return cache[query]

            if current > target:
                return 0
            
            if i == size:
                return current
            

            a = dfs(i + 1, current + stones[i])
            b = dfs(i + 1, current)

            
            cache[query] = max(a, b)

            return cache[query]

        left = dfs()
        right = total - left
        return abs(left - right)



            



