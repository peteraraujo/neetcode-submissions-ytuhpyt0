class Solution:
    def shipWithinDays(self, weights: List[int], maxdays: int) -> int:
        
        maxcap = sum(weights)
        mincap = max(weights)

        l, r = mincap, maxcap

        def getDays(cap):
            days = 1
            left = cap
            for w in weights:
                if left - w < 0:
                    days += 1
                    left = cap
                left -= w
            return days

        while l <= r:
            
            midcap = (l + r) // 2

            days = getDays(midcap)

            if days <= maxdays:
                r = midcap - 1
            else:
                l = midcap + 1
        
        return l








