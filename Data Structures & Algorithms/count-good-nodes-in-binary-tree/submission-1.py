# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node=root, maxx=float("-inf")):

            if not node:
                return 0

            res = (1 if node.val >= maxx else 0) + dfs(node.left, max(maxx, node.val)) + dfs(node.right, max(maxx, node.val))

            return res
        
        return dfs()

