class Solution:
    separator = "#"

    def encode(self, strs: List[str]) -> str:
        return "".join([ str(len(word)) + self.separator + word for word in strs ])


    def decode(self, s: str) -> List[str]:
        print(f"{s=}")
        res = []
        i = 0

        while (newI := s.find(self.separator, i)) != -1:

            print(f"{s[i : newI]=}")
            count = int(s[i : newI])
            word = s[newI + 1 : newI + 1 + count]
            print(f"{word=}")
            res.append(word)
            
            i = newI + 1 + count

            print(f"i after change = {i=} | {newI=}")
        
        return res
