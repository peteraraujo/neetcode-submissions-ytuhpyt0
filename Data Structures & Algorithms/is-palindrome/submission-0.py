class Solution:
    def isPalindrome(self, s: str) -> bool:

        l = 0
        r = len(s) - 1

        while l < r:
            while not s[l].isalnum() and l + 1 < r:
                l += 1
            
            while not s[r].isalnum() and l < r - 1:
                r -= 1
            
            if s[l].isalnum() and s[r].isalnum():
                if s[l].lower() != s[r].lower():
                    return False
            
            l += 1
            r -= 1
        
        return True
