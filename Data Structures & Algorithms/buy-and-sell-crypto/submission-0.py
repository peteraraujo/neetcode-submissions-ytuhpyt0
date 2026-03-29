class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        
        low = prices[0]
        high = 0
        earning = 0

        for i in range(1, size):
            price = prices[i]

            if price < low:
                earning = max(earning, high - low)
                low = price
                high = price

            high = max(high, price)
        
        earning = max(earning, high - low)

        return earning

            