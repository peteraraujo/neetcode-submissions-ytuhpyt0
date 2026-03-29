class Solution:
    def isHappy(self, n: int) -> bool:

        visited = set()

        while n != 1:
            
            digits = []
            while n > 0:
                digits.append(n % 10)
                n //= 10

            val = sum(map(lambda x: x**2, digits))
            
            if val in visited:
                return False
            
            visited.add(val)
            
            n = val
        
        return True

