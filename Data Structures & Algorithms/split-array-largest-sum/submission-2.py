class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        size = len(nums)

        ps = [0] * (size + 1)

        for i in range(size):
            ps[i + 1] = ps[i] + nums[i]

        def canSplit(largest):
            subcount = 0

            i = 0
            while i < size:
                l, r = i + 1, size

                while l <= r:
                    mid = (l + r) // 2
                    if ps[mid] - ps[i] <= largest:
                        l = mid + 1
                    else:
                        r = mid - 1
            
                subcount += 1
                i = r

                if subcount > k:
                    return False
            
            return True
                

        l, r = max(nums), sum(nums)

        res = r

        while l <= r:
            mid = (l + r) // 2

            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res


