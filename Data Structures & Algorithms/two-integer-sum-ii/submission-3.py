class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        size = len(numbers)
        l, r = 0, size - 1

        while l < r:
            t = numbers[l] + numbers[r]
            if t == target:
                return [l + 1, r + 1]
            if t < target:
                l += 1
            else:
                r -= 1
            
