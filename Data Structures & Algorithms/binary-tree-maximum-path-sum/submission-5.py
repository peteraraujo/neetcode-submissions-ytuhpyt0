# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def dfs(n):
            if not n:
                return 0
            
            nonlocal res

            leftVal, rightVal = dfs(n.left), dfs(n.right)

            nodeOnly = n.val
            nLeft = n.val + leftVal
            nRight = n.val + rightVal
            bothPaths = n.val + leftVal + rightVal

            currentPath = max(nodeOnly, nLeft, nRight, bothPaths)
            res = max(res, currentPath)
            
            
            return max(nodeOnly, nLeft, nRight)
        
        dfs(root)
        return res
