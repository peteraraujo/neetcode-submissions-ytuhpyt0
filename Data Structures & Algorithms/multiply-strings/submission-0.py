class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        def num(s):
            base = 48
            size = len(s)

            no = 0

            for i in range(size):
                n = ord(s[i]) - base
                n = n * (10 ** (size - (i + 1)))
                no += n

            return no

        return str(num(num1) * num(num2))

        