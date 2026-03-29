from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        cs = Counter(nums)
        res = []

        for e, c in cs.most_common():
            if c > len(nums) / 3:
                res.append(e)
        
        return res