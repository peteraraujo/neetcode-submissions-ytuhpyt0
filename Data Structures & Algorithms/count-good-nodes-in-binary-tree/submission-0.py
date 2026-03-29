# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root:
            return 0

        res = 1

        def dfs(node, maxVal):
            
            nonlocal res

            if not node:
                return
            
            if node.val >= maxVal:
                res +=1 
                dfs(node.left, node.val)
                dfs(node.right, node.val)
            else:
                dfs(node.left, maxVal)
                dfs(node.right, maxVal)

        dfs(root.left, root.val)
        dfs(root.right, root.val)

        return res



