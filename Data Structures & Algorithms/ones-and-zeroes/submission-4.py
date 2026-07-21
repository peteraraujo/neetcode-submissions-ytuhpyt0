class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        strs = [ Counter(s) for s in strs ]

        size = len(strs)

        cache = {}

        def dfs(i=0, zeros=0, ones=0):

            if zeros > m or ones > n:
                return float("-inf")

            if i == size:
                return 0

            
            query = (i, zeros, ones)

            if query in cache:
                return cache[query]
            
            a = dfs(i + 1, zeros + strs[i]["0"], ones + strs[i]["1"]) + 1
            b = dfs(i + 1, zeros, ones)

            cache[query] = max(a, b)
            return cache[query]

            

        return dfs()
        

        



        



            