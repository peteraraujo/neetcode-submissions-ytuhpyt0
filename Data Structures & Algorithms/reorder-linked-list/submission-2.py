# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return

        prev = s = f = head
        while f and f.next:
            prev = s
            s = s.next
            f = f.next.next

        prev.next = None

        cur = s
        prev = None

        while cur:
            temp = cur.next
            cur.next = prev

            prev = cur
            cur = temp
        
        cur = head
        l = head.next
        r = prev
        
        while l or r:
            if r:
                cur.next = r
                cur = cur.next
                r = r.next
            if l:
                cur.next = l
                cur = cur.next
                l = l.next
                
            

        