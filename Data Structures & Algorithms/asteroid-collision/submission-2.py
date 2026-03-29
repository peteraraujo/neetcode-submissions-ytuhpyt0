class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for n in asteroids:
            
            if stack and stack[-1] >= 0 and n < 0 and abs(stack[-1]) == abs(n):
                stack.pop()
                continue

            destroyed = False

            while stack and stack[-1] >= 0 and n < 0 and abs(n) >= abs(stack[-1]):
                if abs(n) == abs(stack[-1]):
                    stack.pop()
                    destroyed = True
                    break
                else:
                    stack.pop()
            
            if destroyed:
                continue

            if stack and stack and stack[-1] >= 0 and n < 0 and abs(stack[-1]) > abs(n):
                continue
            
            stack.append(n)
            
        return stack


            
                

        
            