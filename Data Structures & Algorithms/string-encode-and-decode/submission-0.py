class Solution:

    delimeter = "#"

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + self.delimeter + s

        return res



    def decode(self, s: str) -> List[str]:
        res = []

        l = 0

        while (r := s.find(self.delimeter, l)) != -1:

            length = int(s[l:r])

            l = r + 1 + length

            res += [s[r + 1:l]]
        
        return res










