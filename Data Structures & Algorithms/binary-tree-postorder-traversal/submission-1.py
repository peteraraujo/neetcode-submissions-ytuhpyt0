# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [(root, False, False)]
        res = []

        if not root:
            return res

        while stack:
            cur, left, right = stack.pop()

            if not left:
                stack.append((cur, True, right))
                if cur.left:
                    stack.append((cur.left, False, False))
            
            elif not right:
                stack.append((cur, left, True))
                if cur.right:
                    stack.append((cur.right, False, False))
            else:
                res.append(cur.val)
        
        return res



            