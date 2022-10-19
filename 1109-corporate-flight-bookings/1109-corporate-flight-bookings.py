class Solution:
    def corpFlightBookings(self, bookings, n: int):
        arr = [0] * n
        for start,end,seats in bookings:
            arr[start-1] += seats
            if end < n:
                arr[end] -= seats
                
        for i in range(1, len(arr)):
            arr[i] += arr[i-1]
        
        return arr
            