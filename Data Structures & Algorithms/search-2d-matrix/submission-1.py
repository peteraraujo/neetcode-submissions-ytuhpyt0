class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l, r = 0, len(matrix) - 1

        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] <= target:
                l = m + 1
            else:
                r = m - 1
        
        if l - 1 == -1:
            return False
        
        arr = matrix[l-1]
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            if arr[m] == target:
                return True
            if arr[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return False
                
        


        # target = 650
        # 10, 20, 40, 50, 700, 1233, 8000