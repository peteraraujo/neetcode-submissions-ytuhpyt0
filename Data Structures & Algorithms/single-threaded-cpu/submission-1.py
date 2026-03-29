# pt = processing time

from heapq import heappush, heappop, heapify
from collections import defaultdict
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        
        available = defaultdict(list) # processingTime: [index]
        availableOrder = [] # processingTime

        tasks = [ [tasks[i][0], tasks[i][1], i] for i in range(len(tasks)) ]

        heapify(tasks)

        def addTasks():
            while tasks and tasks[0][0] <= tick:
                enq, pt, idx = heappop(tasks)
                
                # Add task
                heappush(availableOrder, pt)
                heappush(available[pt], idx)
        
        def processNext():
            nonlocal tick

            

            # Get next shortest processing time
            nextpt = heappop(availableOrder)

            # Add it to res
            res.append(heappop(available[nextpt]))

            # Update tick
            tick += nextpt
        
        tick = tasks[0][0]
        for _ in range(len(tasks)):
            addTasks()
            processNext()

            if not availableOrder and tasks and tasks[0][0] > tick:
                tick = tasks[0][0]
        
        
        
        return res
        
        



