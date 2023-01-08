import heapq

class Solution:
    def carPooling(self, trips, capacity: int) -> bool:
        trips.sort(key=lambda trip:trip[1])

        minHeap = []
        currPassengers = 0
        for trip in trips:
            numPass, start, end = trip
            while minHeap and minHeap[0][0] <= start:
                val = heapq.heappop(minHeap)
                currPassengers -= val[1]
            
            currPassengers += numPass
            if currPassengers > capacity:
                return False
            heapq.heappush(minHeap, [end, numPass])
        
        return True
