class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        size = len(nums)
        ps = [0] * (size + 1)

        for i in range(size):
            ps[i + 1] = ps[i] + nums[i]
        
        for i in range(1, size + 1):
            if ps[i - 1] == ps[-1] - ps[i]:
                return i - 1
        
        return -1        