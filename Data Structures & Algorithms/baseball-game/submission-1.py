class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        cur = 0

        for o in operations:
            try:
                new = int(o)
                stack.append(new)
                cur += new
            except:
                if o == '+':
                    new = stack[-2] + stack[-1]
                    stack.append(new)
                    cur += new
                elif o == 'D':
                    new = stack[-1] * 2
                    stack.append(new)
                    cur += new
                else:
                    cur -= stack.pop()
        
        return cur