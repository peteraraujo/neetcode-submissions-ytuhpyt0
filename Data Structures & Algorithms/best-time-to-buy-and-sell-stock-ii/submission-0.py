class Solution:
    def maxProfit(self, prices: List[int]) -> int:        
        stack = []
        res = 0

        for n in prices:
            if not stack:
                stack.append(n)
                continue

            if n < stack[-1]:
                res += stack[-1] - stack[0]

                stack.clear()
                stack.append(n)
            
                continue
            
            stack.append(n)
                
        
        res += stack[-1] - stack[0]

        return res
            
            

