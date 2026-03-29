class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        tens = 0
        fives = 0

        for b in bills:
            if b == 10:
                tens += 1
            elif b == 5:
                fives += 1

            change = b - 5

            if change >= 10 and tens > 0:
                change -= 10
                tens -= 1
            fives -= change // 5
            
            if fives < 0:
                return False

            
        
        return True
            