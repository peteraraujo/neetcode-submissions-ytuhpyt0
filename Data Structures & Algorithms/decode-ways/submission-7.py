class Solution:
    def numDecodings(self, s: str) -> int:
        size = len(s)

        visited = {} # subs -> # of arranges

        def dfs(sub):            
            if not sub:
                return 1

            if sub[0] == "0":
                return 0

            if sub in visited:
                return visited[sub]
            
            temp = 0

            temp += dfs(sub[1:])

            if len(sub) > 1:
                a, b = sub[0], sub[1]

                if ((a == "1") or (a == "2" and b not in ("7", "8", "9"))):
                    temp += dfs(sub[2:])
            
            visited[sub] = temp

            return temp

        r = dfs(s)
        print(visited)

        return r
            




            


            
            

