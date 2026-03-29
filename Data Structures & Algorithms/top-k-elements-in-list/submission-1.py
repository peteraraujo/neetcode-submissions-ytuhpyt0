class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        from collections import Counter
        c = Counter(nums)
        return list(map(lambda entry: entry[0], c.most_common(k)))







        