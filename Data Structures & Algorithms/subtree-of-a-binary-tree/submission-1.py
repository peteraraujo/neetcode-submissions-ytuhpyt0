# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root:
            return not subRoot

        def check(node1, node2):
            if not node1:
                return not node2
            if not node2:
                return not node1
            
            return node1.val == node2.val \
            and check(node1.left, node2.left) \
            and check(node1.right, node2.right)

        return check(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)