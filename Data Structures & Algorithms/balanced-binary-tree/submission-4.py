# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            # Base case: if node is None, return height 0
            if not node:
                return 0
            
            # Get heights of left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)
            
            # If either subtree is unbalanced (returns -1) or current node is unbalanced
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
                
            # Return height of current node
            return 1 + max(left, right)
        
        # Return True if dfs returns a non-negative number (valid height)
        return dfs(root) != -1
            
