# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        flippable = [] # [start, end]
        static = None # start

        l = r = head

        rem = k - 1

        while l:

            if rem:
                r = r.next
                rem -= 1
                
                if not r:
                    static = l
                    break
                continue
            
            # No rem
            
            # Save pointers
            flippable.append([l, r])

            l = r.next
            r.next = None
            r = l
            rem = k - 1


        # print( [[p.val for p in pointers] for pointers in flippable], static.val if static else None)
        
        for start, end in flippable:
            cur = start
            prev = None

            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
        

        for i in range(1, len(flippable)):
            s1, e1 = flippable[i - 1]
            s2, e2 = flippable[i]

            s1.next = e2

        flippable[-1][0].next = static

        return flippable[0][1]




