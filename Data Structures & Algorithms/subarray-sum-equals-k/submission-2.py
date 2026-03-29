from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pcs = defaultdict(int)

        pcs[0] += 1

        s = 0
        res = 0

        for n in nums:
            s += n

            diff = s - k
            res += pcs.get(diff, 0)

            pcs[s] += 1
        
        return res
            



