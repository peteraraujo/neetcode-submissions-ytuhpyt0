# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        # Return (prev, cur)
        def dfs(prev=None, node=root):

            if not node:
                return (None, None)

            if node.val == key:
                return (prev, node)


            if node.val < key:
                return dfs(node, node.right)
            else:
                return dfs(node, node.left)
            
        # Search node
        prev, node = dfs()
        
        # Case: Node not found
        if not node:
            return root


        # Get children nodes
        left, right = node.left, node.right

        # Determine which node will be connected with parent
        connectingNode = right if not left else left
        searchNode = right if left else left
        
        # Connect prev with connectingNode
        if prev:
            if node.val < prev.val:
                # Connect left
                prev.left = connectingNode
            else:
                # Connect right
                prev.right = connectingNode

        # Reassign root if key is root
        if root == node:
            root = connectingNode
        
        # Return if not search node
        if not searchNode:
            return root
        
        # Search insertion node
        searchPrev = connectingNode

        # Search node is left node
        if searchNode.val < connectingNode.val:

            while searchPrev.left:
                searchPrev = searchPrev.left
            
            searchPrev.left = searchNode
        
        # Search node is right node
        else:
            
            while searchPrev.right:
                searchPrev = searchPrev.right
            
            searchPrev.right = searchNode
        
        return root

        



















            
        

