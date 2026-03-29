class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        res = []
        temp = []

        def dfs(i):
            if i >= len(digits):
                res.append("".join(temp))
                return
            
            for c in self.digitToChars(digits[i]):
                temp.append(c)
                dfs(i + 1)
                temp.pop()
        
        dfs(0)
        return res
    
    


    def digitToChars(self, digit):
        match digit:
            case '2':
                return "abc"
            case '3':
                return "def"
            case '4':
                return "ghi"
            case '5':
                return "jkl"
            case '6':
                return "mno"
            case '7':
                return "pqrs"
            case '8':
                return "tuv"
            case '9':
                return "wxyz"