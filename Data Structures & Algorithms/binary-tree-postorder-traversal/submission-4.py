# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [[root, False]]

        if not root:
            return []

        res = []

        while stack:
            cur = stack[-1]
            if cur[1] == True:
                res.append(stack[-1][0].val)
                stack.pop()
            else:
                stack[-1][1] = True
                if n := cur[0].right:
                    stack.append([n, False])
                if n := cur[0].left:
                    stack.append([n, False])
            
                
        
        return res
