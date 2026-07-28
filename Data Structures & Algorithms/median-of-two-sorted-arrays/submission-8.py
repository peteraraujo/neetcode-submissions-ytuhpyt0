class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        size1 = len(nums1)
        size2 = len(nums2)

        if size1 > size2:
            return self.findMedianSortedArrays(nums2, nums1)

        total = size1 + size2
        half = total // 2
        even = total % 2 == 0

        l, r = 0, size2

        while l <= r:
            # First element on the right
            m = (l + r) // 2

            left1index = half - m - 1
            right1index = half - m

            left2index = m -1
            right2index = m

            nleft1 = nums1[left1index] if 0 <= left1index < size1 else float("-inf")
            nright1 = nums1[right1index] if 0 <= right1index < size1 else float("inf")

            nleft2 = nums2[left2index] if 0 <= left2index < size2 else float("-inf")
            nright2 = nums2[right2index] if 0 <= right2index < size2 else float("inf")

            if nleft1 <= nright2 and nleft2 <= nright1:
                return min(nright1, nright2) if not even else ((max(nleft1, nleft2) + min(nright1, nright2)) / 2)
            
            if nright2 < nleft1:
                l = m + 1
            else:
                r = m - 1
        

        return -1

