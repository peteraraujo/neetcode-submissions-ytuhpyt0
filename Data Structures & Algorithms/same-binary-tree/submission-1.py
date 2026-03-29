# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(r1, r2):

            if not r1:
                return not r2
            if not r2:
                return not r1

            if r1.val != r2.val:
                return False
            
            return dfs(r1.left, r2.left) and dfs(r1.right, r2.right)
        
        return dfs(p, q)