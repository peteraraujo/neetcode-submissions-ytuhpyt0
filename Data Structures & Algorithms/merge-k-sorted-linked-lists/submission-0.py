# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heappop as hpop, heappush as hpush

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dm = ListNode(0)
        cur = dm

        # (value, list index)

        mh = [(l.val, i) for i, l in enumerate(lists)]
        heapq.heapify(mh)

        while mh:
            val, i = hpop(mh)

            cur.next = ListNode(val)
            cur = cur.next
            lists[i] = lists[i].next

            if lists[i]:
                hpush(mh, (lists[i].val, i))
        
        
        return dm.next


            


