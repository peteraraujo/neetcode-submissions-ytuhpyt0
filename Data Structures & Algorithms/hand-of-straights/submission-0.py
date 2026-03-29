class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        heapq.heapify(hand)
        leftovers = []

        for _ in range(len(hand) // groupSize):
            print("Hand:", hand)
            print("Leftovers:",leftovers)
            last = heapq.heappop(hand)
            
            for _ in range(groupSize - 1):
                

                current = heapq.heappop(hand)

                while hand and current == last:
                    leftovers.append(current)
                    current = heapq.heappop(hand)

                if current != last + 1:
                    return False

                last = current
            
            
            hand.extend(leftovers)
            heapq.heapify(hand)
            leftovers.clear()

    
        return True

