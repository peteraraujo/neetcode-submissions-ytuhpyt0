class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)

        maxw = l = 0
        w = set()

        for r in range(size):
            while s[r] in w:
                w.remove(s[l])
                l += 1
            w.add(s[r])
            maxw = max(maxw, len(w))

        return maxw
