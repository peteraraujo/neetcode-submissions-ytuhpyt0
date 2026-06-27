class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        size = len(s)
        
        l = 0
        cs = Counter()

        res = 0

        for r in range(size):
            cs[s[r]] += 1

            while l < r and ((r - l) + 1) - cs.most_common(1)[0][1] > k:
                cs[s[l]] -= 1
                l += 1

            res = max(res, (r - l) + 1)
        
        return res

