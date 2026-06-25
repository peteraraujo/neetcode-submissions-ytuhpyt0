class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dq = deque([[0, 0]])
        visited = set()

        while dq:
            cur, step = dq.popleft()

            if cur in visited or cur > amount:
                continue

            if cur == amount:
                return step

            visited.add(cur)


            for coin in coins:
                dq.append([cur + coin, step + 1])
        
        return -1
        
