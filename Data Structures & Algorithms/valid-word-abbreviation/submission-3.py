import re

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        abbr = re.findall(r"[A-Za-z]+|\d+", abbr)
        print(abbr)

        i = 0

        for a in abbr:
            if a.isalpha():
                if a != word[i:i + len(a)]:
                    return False
                else:
                    i += len(a)
            
            elif a.isnumeric():
                i += int(a)
                if i > len(word) or a[0] == "0":
                    return False
            
            print(f"{i=} | {a=}")
        
        return i == len(word)





        