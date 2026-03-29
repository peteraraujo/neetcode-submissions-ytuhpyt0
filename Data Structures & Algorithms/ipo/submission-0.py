from heapq import heappush as push, heappop as pop

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        size = len(profits)
        cp = [ (capital[i], profits[i]) for i in range(size) ] # (capital, profit)
        heapq.heapify(cp)

        pc = []

        for _ in range(k):
            print(f"Before: {w=} {cp=}")
            while cp and w >= cp[0][0]:
                root = pop(cp)
                push(pc, (-root[1], root[0]))
            
            if not pc:
                return w
            
            w += -pop(pc)[0]

            print(f"After: {w=}")

        return w
