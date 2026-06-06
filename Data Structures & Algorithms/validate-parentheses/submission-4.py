class Solution:

    BRACKETS = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    def isValid(self, s: str) -> bool:

        history = []

        for bracket in s:
            if bracket not in Solution.BRACKETS:
                history.append(bracket)
                
            
            elif not history or Solution.BRACKETS[bracket] != history.pop():
                return False
        
        return not history
        