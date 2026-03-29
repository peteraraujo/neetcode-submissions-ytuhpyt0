# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True

        def dfs(current):

            if current is None:
                return 0
            
            left = dfs(current.left)
            right = dfs(current.right)

            if (abs(left - right) > 1):
                raise Exception()
        
            return 1 + max(left, right)
        
        try:
            dfs(root)
        except:
            return False
        else:
            return True


        
