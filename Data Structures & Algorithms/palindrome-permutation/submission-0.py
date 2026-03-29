from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        c = Counter(s)
        w = True

        for v in c.values():
            if v % 2 != 0:
                if w:
                    w = False
                else:
                    return False
        
        return True
















