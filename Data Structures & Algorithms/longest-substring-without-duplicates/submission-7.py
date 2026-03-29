class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res = 0
        chars = {} # char: index

        l = 0
        
        for r in range(len(s)):
            char = s[r]
            if char in chars:
                res = max(res, len(chars))
                while s[l] != char:
                    del chars[s[l]]
                    l += 1
                del chars[s[l]]
                l += 1
            chars[char] = r
        
        res = max(res, len(chars))
        return res



