class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda interval: interval[0])
        size = len(intervals)
        merged = []
        for i in range(size):
            if i == 0 or merged[-1][1] < intervals[i][0]:
                merged.append(intervals[i])
            else:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
        
        return merged