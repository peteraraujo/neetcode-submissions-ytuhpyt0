class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l, r = 0, len(numbers) - 1

        while l < r:
            n = numbers[l] + numbers[r]
            if n == target:
                return [l + 1, r + 1]
            
            if n > target:
                
                while l < r - 1 and numbers[r - 1] == numbers[r]:
                    r -= 1
                r -= 1
            else:
                while l + 1 < r and numbers[l + 1] == numbers[l]:
                    l += 1
                l += 1