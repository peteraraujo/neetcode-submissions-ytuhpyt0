# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        res = f"{root.val}#"

        queue = deque([root])

        while queue:
            
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                    res += f"{node.left.val}#"
                else:
                    res += "n#"

                if node.right:
                    queue.append(node.right)
                    res += f"{node.right.val}#"
                else:
                    res += "n#"

        
        print(res)
        return res

        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        def values(data):
            start = 0
            while (nextMarker := data.find("#", start)) != -1:

                yield data[start:nextMarker]
                
                start = nextMarker + 1

        values = values(data)

        root = TreeNode(next(values))

        queue = deque([root])

        while queue:

            for _ in range(len(queue)):
                node = queue.popleft()

                if (val := next(values)) != "n":
                    node.left = TreeNode(val)
                    queue.append(node.left)
                if (val := next(values)) != "n":
                    node.right = TreeNode(val)
                    queue.append(node.right)
        
        return root


        
        







        


        
        
