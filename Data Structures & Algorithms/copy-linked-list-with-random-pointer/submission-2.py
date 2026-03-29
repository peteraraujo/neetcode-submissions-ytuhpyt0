"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # og: new
        ognew = {}

        dummy = Node(0)
        newcur = dummy
        cur = head

        while cur:
            
            new = ognew[cur] if cur in ognew else Node(cur.val)
            ognew[cur] = new
            random = None if not cur.random else ognew[cur.random] if cur.random in ognew else Node(cur.random.val)
            if random:
                ognew[cur.random] = random
            
            new.random = random
            

            newcur.next = new
            

            cur = cur.next
            newcur = newcur.next
        
        return dummy.next





