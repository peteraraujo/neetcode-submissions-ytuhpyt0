class Solution:
    def decodeString(self, si: str) -> str:

        def dfs(s):
            res = []
            
            i = 0
            while i < len(s):
                if s[i].isalpha():
                    res.append(s[i])
                    i += 1
                    continue
                elif s[i].isdigit():
                    bracket = s.find('[', i + 1)
                    n = int(s[i:bracket])
                    i = bracket + 1
                    o = 1

                    # This'll stop at the next char of the correcponding "]"
                    while o > 0:
                        if s[i] == "[":
                            o += 1
                        elif s[i] == "]":
                            o -= 1
                        i += 1

                    parsed = dfs(s[bracket + 1 : i - 1]) * n
                    res.append(parsed)
            return "".join(res)
        
        return dfs(si)
                    


                    

        

        







