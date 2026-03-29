class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k < 1:
            return False

        size = len(nums)
        
        w = set()
        
        l = 0

        for i in range(size):

            print(f"{i=} | {l=}")

            if i - l > k:
                w.remove(nums[l])
                l += 1
            
            if nums[i] in w:
                return True
            
            w.add(nums[i])
        
        return False



