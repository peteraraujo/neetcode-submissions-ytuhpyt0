# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        
        newHead = None

        prev = None

        left = head
        right = head
        nextNode = head.next

        while left:
            
            for _ in range(k - 1):
                if not nextNode:
                    return newHead if newHead else head
                
                right = nextNode
                nextNode = nextNode.next if nextNode else None

            localprev = nextNode
            cur = left

            for _ in range(k):
                temp = cur.next
                cur.next = localprev

                localprev = cur
                cur = temp
            
            if not newHead:
                newHead = localprev
            
            if prev:
                prev.next = right
            
            prev = left
            left = right = nextNode
            nextNode = right.next if right else None
        
        return newHead if newHead else head
            


