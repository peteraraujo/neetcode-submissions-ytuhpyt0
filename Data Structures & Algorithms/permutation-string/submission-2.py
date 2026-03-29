class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False
        
        cs1 = [0] * 26
        cs2 = [0] * 26

        for char in s1:
            cs1[ord(char) - ord("a")] += 1
        
        cs1 = tuple(cs1)

        for i in range(len(s1) - 1):
            cs2[ord(s2[i]) - ord("a")] += 1

        for l in range(len(s1) - 1, len(s2)):
            
            lChar = s2[l - (len(s1) - 1)]
            rChar = s2[l]
            print(f"{l=} - {lChar=} - {rChar=}")

            cs2[ord(rChar) - ord("a")] += 1
            if tuple(cs2) == cs1:
                return True
            
            cs2[ord(lChar) - ord("a")] -= 1
        
        return False


            


        