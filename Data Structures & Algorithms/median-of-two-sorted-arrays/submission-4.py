class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        size1, size2 = len(nums1), len(nums2)
        
        if size1 > size2:
            return self.findMedianSortedArrays(nums2, nums1)
        
        total = size1 + size2
        half = total // 2
        even = total % 2 == 0



        l, r = 0, size2 # number of items of nums2 in left side

        while l <= r:
            leftcountfornums2 = (l + r) // 2

            i2, j2 = leftcountfornums2 - 1, leftcountfornums2
            i1, j1 = half - leftcountfornums2 - 1, half - leftcountfornums2

            n1l, n1r = nums1[i1] if 0 <= i1 < size1 else float('-inf'), nums1[j1] if 0 <= j1 < size1 else float('inf')
            n2l, n2r = nums2[i2] if 0 <= i2 < size2 else float('-inf'), nums2[j2] if 0 <= j2 < size2 else float('inf')
            
            if n1l <= n2r and n2l <= n1r:
                if even:
                    return (max(n1l, n2l) + min(n1r, n2r)) / 2
                else:
                    return min(n1r, n2r)

            if n1l > n2r:
                l = leftcountfornums2 + 1
                
            else:
                r = leftcountfornums2 - 1





