from heapq import heappush, heappop, heapify

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        cs = Counter()

        # (endTime, room)
        busyRooms = []

        availableRooms = [room for room in range(n)]

        for meetingStart, meetingEnd in meetings:
            endDelta = meetingEnd - meetingStart

            while (busyRooms and busyRooms[0][0] <= meetingStart):
                heappush(availableRooms, heappop(busyRooms)[1])

            if not availableRooms:
                availableTime, room = heappop(busyRooms)
                meetingStart = availableTime
            else:
                room = heappop(availableRooms)

            cs[room] += 1

            heappush(busyRooms, (meetingStart + endDelta, room))


        

        uses = cs.most_common()
        maxUses = uses[0][1]
        minRoom = uses[0][0]

        for room, use in uses:
            if use < maxUses:
                break
            
            minRoom = min(minRoom, room)

        return minRoom