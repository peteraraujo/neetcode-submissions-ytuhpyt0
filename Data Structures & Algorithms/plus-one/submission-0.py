class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        i = len(digits) - 1

        while i >= 0:
            digits[i] = (digits[i] + 1) % 10

            if digits[i] != 0:
                return digits
            
            i -= 1

        return [1] + digits



