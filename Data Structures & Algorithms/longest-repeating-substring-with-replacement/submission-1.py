class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cs = [0] * 26
        res = 0

        l = 0

        for r in range(len(s)):

            cs[ord(s[r]) - ord("A")] += 1

            while ((r - l) + 1) - max(cs) > k:
                cs[ord(s[l]) - ord("A")] -= 1
                l += 1

            res = max(res, (r - l) + 1)


        return res 
       
            

