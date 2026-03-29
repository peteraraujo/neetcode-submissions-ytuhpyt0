from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadend = set(deadends)

        dirs = []
        for i in range(8):
            val = 1 if i < 4 else -1
            temp = []
            for j in range(4):
                temp.append(val if j == (i % 4) else 0)

            dirs.append(tuple(temp))

        dq = deque([(0, (0, 0, 0, 0))])
        steps = 0
        failed = set()

        while dq:
            children = []
            for _ in range(len(dq)):
                step, cur = dq.popleft()
                string = "".join(map(lambda x: str(x), cur))
                if string in deadend or cur in failed:
                    continue
                if string == target:
                    return steps

                failed.add(cur)

                #steps = step


                for d in dirs:
                    children.append((step+1, tuple([((cur[i] + d[i]) % 10) for i in range(4)])))

            dq.extend(children)
            steps += 1

        return -1