class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isp(sub):
            return sub == ''.join(reversed(sub))

        def dfs(pre, sub):
            size = len(sub)

            if size == 0:
                return [[pre]]

            res = []

            for i in range(size):
                pick = sub[:i + 1]

                if not isp(pick):
                    continue
                


                print(f"{pre=} | {sub=} | {pick=} | {sub[i + 1:]=}")
                suffixes = dfs(pick, sub[i + 1:])
                

                for suffix in suffixes:
                    temp = [] if not pre else [pre]
                    temp.extend(suffix)
                    res.append(temp)
            
            return res
        
        return dfs(None, s)