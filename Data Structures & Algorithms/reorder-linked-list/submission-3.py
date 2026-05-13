# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Middle
        s, f = head, head.next

        while f and f.next:
            s = s.next
            f = f.next.next
        
        # Separate
        cur = s.next
        s.next = None
        
        # Reverse
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev, cur = cur, temp
        

        # Rejoin
        a, b = head, prev
        dummy = cur = ListNode()
        while a and b:
            cur.next = a
            a = a.next
            cur.next.next = b
            b = b.next
            cur = cur.next.next
        
        if a:
            cur.next = a
        if b:
            cur.next = b
        
        

        

        

