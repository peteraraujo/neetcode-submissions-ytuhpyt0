# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    delimeter = "-"
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        lt = []

        q = deque([root])

        while q:
            node = q.popleft()

            if not node:
                lt.append(None)
                continue

            lt.append(node.val)

            q.append(node.left)
            q.append(node.right)

        lt = [ str(item) for item in lt ]

        return Codec.delimeter.join(lt)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        lt = [int(item) if item != "None" else None for item in data.split(Codec.delimeter)]
        
        if not lt or not lt[0]:
            return None

        

        root = TreeNode(lt[0])
        root.left = TreeNode(lt[1]) if lt[1] else None
        root.right = TreeNode(lt[2]) if lt[2] else None

        i = 3

        q = deque([root.left, root.right])

        while q and i < len(lt):
            node = q.popleft()

            if not node:
                continue

            if lt[i]:
                node.left = TreeNode(lt[i])
                        
            i += 1
            
            if lt[i]:
                node.right = TreeNode(lt[i])
            i += 1  
            
            q.append(node.left)
            q.append(node.right)
                
        
        
        return root





















