class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        size = len(temperatures)

        stack = []
        res = [0] * size

        for i in range(size - 1, -1, -1):
            temp = temperatures[i]

            while stack and temp >= temperatures[stack[-1]]:
                stack.pop()
            
            
            res[i] = stack[-1] - i if stack else 0

            stack.append(i)



        return res
