# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # 1 -> 2 -> 3 -> | None <- 4 <- 3 <- 2 <- 1
        # 1 -> 2 -> 3 -> | None <- 3 <- 2 <- 1

        s = head
        f = head
        
        while f:
            
            s = s.next
            f = f.next
            if f:
                f = f.next
        
        cur = s
        prev = None
        n = cur.next if cur else None

        while cur:
            cur.next = prev
            prev = cur
            cur = n
            n = cur.next if cur else None
        
        l = head
        r = prev
        
        while r and l is not r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next

        return True


            







