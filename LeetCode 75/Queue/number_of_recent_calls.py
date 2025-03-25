from collections import deque


class RecentCounter:

    def __init__(self):
        self.recent_requests = deque()
    
    def ping(self, t: int) -> int:
        self.recent_requests.append(t)

        while t - 3000 > self.recent_requests[0]:
            self.recent_requests.popleft()

        return len(self.recent_requests)
    
    """
    Time Complexity Analysis:
    Step 1: Understanding the Worst Case for One ping Call
        When calling ping(t), we do two main operations:
        -> Append t to self.recent_requests → This is always O(1).
        -> Remove outdated requests from the deque: The while loop removes elements from the front of the deque if they are older than t - 3000.

        In the worst case, all past requests are removed, meaning we may pop up to N elements in one call 
        (where N is the current size of the deque).
        This makes the worst-case complexity of one call O(N).

    Step 2: Why We Need to Consider Amortized Complexity
        Instead of looking at the worst case for a single call, amortized analysis looks at the total number of operations across multiple calls and divides it evenly.
        The key idea:
        -> Each request is added exactly once (when it is first appended to the deque).
        -> Each request is removed at most once (when it gets too old and is popped from the front).
        -> This means each request contributes at most one append and one remove to the total operations.
    Step 3: Let's calculate the Amortized Time Complexity
        Total Number of Operations Over Q Calls
        -> In Q calls, we insert Q elements into the deque (one per call).
        -> We also remove at most Q elements across all calls (each element is removed once).
        -> Thus, the total number of operations across all calls is at most 2Q.

        Per Call Amortized Cost
        -> Since the total number of operations is at most O(Q) over Q calls,
        The average number of operations per call is O(Q)/Q=O(1).
    
    Finally:
    Worst-case per call: O(N) (if many elements need to be removed).
    Total over Q calls: O(Q).
    Amortized per call: O(1).

    Space Complexity:
    -> Since we only store requests from the last 3000 milliseconds, the space complexity is O(W), 
    where W is the number of requests in a 3000ms window

    """
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)