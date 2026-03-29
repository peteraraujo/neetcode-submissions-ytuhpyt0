class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        l = []

        while x > 0:
            l.append(x % 10)
            x //= 10
        
        lf = 0
        r = len(l) - 1
        
        while lf < r:
            if l[lf] != l[r]:
                return False
            lf += 1
            r -= 1

        return True
        