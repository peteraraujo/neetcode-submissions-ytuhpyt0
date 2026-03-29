class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        path = path.split("/")
        print(path)

        for p in path:
            if not p:
                continue
                
            if p == ".":
                continue
            
            if p == "..":
                if stack:
                    stack.pop()
                continue

            if not stack:
                stack.append(p)
                continue
            
            stack.append(p)
        
        return "/" + "/".join(stack)