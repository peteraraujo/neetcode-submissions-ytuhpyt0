# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if right - left == 0:
            return head
        
        headdummy = ListNode(0, head)
        leftconn = headdummy
        cur = head

        for _ in range(left-1):
            leftconn = cur
            cur = cur.next
        
        innerrightcon = cur
        
        prev = None
        for _ in range((right - left) + 1):
            temp = cur.next
            cur.next = prev

            prev = cur
            cur = temp

        leftconn.next.next = cur
        leftconn.next = prev

        return headdummy.next



        


        

        


