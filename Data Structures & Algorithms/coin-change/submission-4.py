class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * amount

        for i in range(amount - 1, -1, -1):
            temp = float('inf')

            for c in coins:
                if c + i == amount:
                    temp = 1
                    break
                elif c + i < amount:
                    t = 1 + dp[c + i] if dp[c + i] > 0 else -1
                    if t != -1 and t < temp:
                        temp = t
            
            dp[i] = -1 if temp == float('inf') else temp
        
        print(dp)
        return dp[0] if dp else 0

