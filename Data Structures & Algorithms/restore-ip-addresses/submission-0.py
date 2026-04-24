class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        size = len(s)

        res = []


        def dfs(options=s, stack=[]):
            if len(stack) == 4:
                if not options:
                    res.append(".".join(stack))
                
                return
            
            for io in range(min(3, len(options))):
                option = options[:(io + 1)]

                if len(option) > 1 and option[0] == "0":
                    break
                
                if int(option) > 255:
                    break
                    

                stack.append(option)
                dfs(options[(io + 1): ])
                stack.pop()


        
        dfs()

        return res


            



