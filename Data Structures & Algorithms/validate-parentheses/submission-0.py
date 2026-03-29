class Solution:
    def isValid(self, s: str) -> bool:
        

        stack = []

        options = { ')': '(', ']': '[', '}': '{' }

        for c in s:

            if c in options:
                if not stack or stack[-1] != options[c]:
                    return False
                
                stack.pop()
            else:
                stack.append(c)
        
        return not stack
