class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        c = {}

        for n in nums:
            c[n] = c.get(n, 0) + 1


        return list(map(lambda x: x[0], sorted(c.items(), key=lambda x: x[1], reverse=True)[:k]))