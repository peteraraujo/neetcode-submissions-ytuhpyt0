class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not k:
            return False
        k = min(k, len(nums))
        cs = set()
        
        for i in range(len(nums)):
            if i > k:
                cs.remove(nums[i - (k+1)])

            if nums[i] in cs:
                return True
            cs.add(nums[i])

        return False

        # 1, 0, 1, 1  k = 1
        # 
        