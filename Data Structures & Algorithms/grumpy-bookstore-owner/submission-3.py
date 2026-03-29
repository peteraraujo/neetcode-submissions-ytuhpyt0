class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        size = len(customers)

        happy = 0
        for i in range(size):
            if not grumpy[i]:
                happy += customers[i]

        cur = 0
        for i in range(minutes):
            if grumpy[i]:
                cur += customers[i]

        extra = cur
        for i in range(minutes, size):
            cur -= customers[i - minutes] if grumpy[i - minutes] else 0
            cur += customers[i] if grumpy[i] else 0

            extra = max(extra, cur)

        print(extra)

        return happy + extra



        
    