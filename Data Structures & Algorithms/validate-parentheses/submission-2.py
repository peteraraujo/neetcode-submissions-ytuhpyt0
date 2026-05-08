class Solution:
    def isValid(self, s: str) -> bool:
        ops = {
            ')':'(',
            ']':'[',
            '}':'{',
        }

        stack = []

        for c in s:
            if c in ops:
                if not stack or stack[-1] != ops[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        
        return not stack