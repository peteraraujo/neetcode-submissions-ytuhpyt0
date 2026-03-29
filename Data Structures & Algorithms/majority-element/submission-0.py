class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()

        prev = nums[0]
        res = prev
        count = 1
        curmax = 1

        for i in range(1, len(nums)):
            n = nums[i]
            if n == prev:
                count += 1
            else:
                if count > curmax:
                    res = prev
                    curmax = count
                
                count = 1
                prev = n
        
        if count > curmax:
            res = prev
            curmax = count

        return res      