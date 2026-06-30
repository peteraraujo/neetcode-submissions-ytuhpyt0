# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heappop, heappush

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = current = ListNode(0)

        counter = 0
        
        minheap = []
        for i in range(len(lists)):
            node = lists[i]
            heappush(minheap, (node.val, counter, node))
            counter += 1
        

        while minheap:
            node = heappop(minheap)[2]
            if node.next:
                heappush(minheap, (node.next.val, counter, node.next))
                counter += 1
            current.next = node
            current = current.next
        
        return dummy.next