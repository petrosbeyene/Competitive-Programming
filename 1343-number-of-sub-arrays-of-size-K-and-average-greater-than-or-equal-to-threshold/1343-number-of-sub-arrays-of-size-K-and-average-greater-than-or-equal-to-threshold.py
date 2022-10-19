class Solution:
    def numOfSubarrays(self, arr, k: int, threshold: int) -> int:
        left = 0
        right = k-1
        count = 0
        
        curr_sum = sum(arr[left:right+1])
        while right < len(arr):
            avg = curr_sum / k
            if avg >= threshold:
                count += 1
            if right+1 < len(arr):
                curr_sum += arr[right+1] - arr[left]
            left += 1
            right += 1
        
        return count