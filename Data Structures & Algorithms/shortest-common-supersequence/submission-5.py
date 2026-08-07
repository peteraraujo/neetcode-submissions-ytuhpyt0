class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        size1, size2 = len(str1), len(str2)

        if size1 > size2:
            return self.shortestCommonSupersequence(str2, str1)
        
        row1 = [""] * (size2 + 1)
        row2 = [""] * (size2 + 1)

        for i2 in range(size2):
            row1[i2 + 1] = str2[0 : i2 + 1]
        
        
        

        for i1 in range(size1):
            
            row1[0] = str1[0 : i1]
            row2[0] = str1[0 : i1 + 1]

            for i2 in range(size2):

                r1, r2 = i2 + 1, i2 + 1

                char1, char2 = str1[i1], str2[i2]

                if char1 == char2:
                    row2[r2] = row1[r1 - 1] + char1
                    continue

                path1 = row2[r2 - 1] + char2
                path2= row1[r1] + char1

                row2[r2] = path1 if len(path1) < len(path2) else path2

            row1, row2 = row2, row1
        
    

        return row1[-1]


        
        