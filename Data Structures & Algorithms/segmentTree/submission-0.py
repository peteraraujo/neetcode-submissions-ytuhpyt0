class Node:
    def __init__(self, total, L, R):
        self.sum = total
        self.left = None
        self.right = None
        self.L = L
        self.R = R

class SegmentTree:
    
    def __init__(self, nums: List[int]):
        
        def build(L, R):
            if L == R:
                return Node(nums[L], L, R)
            
            M = (L + R) // 2

            root  = Node(0, L, R)
            root.left = build(L, M)
            root.right = build(M + 1, R)
            root.sum = root.left.sum + root.right.sum

            return root
        
        self.root = build(0, len(nums) - 1)

    
    def update(self, index: int, val: int) -> None:

        def _update(node):

            if node.L == node.R:
                node.sum = val
                return
            
            M = (node.L + node.R) // 2

            if index > M:
                _update(node.right)
            else:
                _update(node.left)
            
            node.sum = node.left.sum + node.right.sum

        _update(self.root)


    def query(self, L: int, R: int) -> int:

        def _query(node, L, R):
            
            if node.L == L and node.R == R:
                return node.sum

            M = (node.L + node.R) // 2

            if L > M:
                return _query(node.right, L, R)
            elif R <= M:
                return _query(node.left, L, R)
            else:
                return _query(node.left, L, M) + _query(node.right, M + 1, R)
        
        return _query(self.root, L, R)













