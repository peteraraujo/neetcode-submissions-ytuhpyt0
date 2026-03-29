class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        res = ""

        def isp(word):
            return word == word[::-1]

        for i in range(size):
            for j in range(size - 1, i - 1, -1):
                sub = s[i:j+1]
                print(sub)
                if isp(sub) and len(sub) > len(res):
                    res = sub
        return res
            


            
