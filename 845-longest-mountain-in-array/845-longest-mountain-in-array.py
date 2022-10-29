class Solution:
    def longestMountain(self, arr) -> int:
        ans,start= 0, 0
        n = len(arr)
        
        while start < n:
            end = start
            if end + 1 < n and arr[end] < arr[end + 1]:
                while end + 1 < n and arr[end] < arr[end+1]:
                    end += 1
                
                if end + 1 < n and arr[end] > arr[end + 1]:
                    while end + 1 < n and arr[end] > arr[end+1]:
                        end += 1
                
                    ans = max(ans, end - start + 1)
                start = end
            else:
                start += 1
        
        return ans