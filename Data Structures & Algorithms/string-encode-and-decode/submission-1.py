class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(list(map(lambda s: str(len(s)) + "#" + s , strs)))


    
    def decode(self, s: str) -> List[str]:
        
        i = 0
        res = []

        while (to := s.find("#", i)) != -1:
            print(to)
            end = to + int(s[i:to])
            res.append(s[to+1:end + 1])
            i = end + 1
        
        return res








