class Solution:
    def numSmallerByFrequency(self, queries, words):
        q_arr = []
        for q in queries:
            curr = min(q)
            q_arr.append(q.count(curr))
        
        w_arr = []
        for w in words:
            curr = min(w)
            w_arr.append(w.count(curr))
        
        ans = []
        w_arr.sort()
        for q in q_arr:
            low, high = 0, len(w_arr)-1
            temp = -1
            while low <= high:
                mid = low + (high - low)//2
                if w_arr[mid] > q:
                    temp = mid
                    high = mid -1
                else:
                    low = mid + 1
            if temp == -1:
                ans.append(0)
            else:
                ans.append(len(w_arr)-temp)
        
        return ans
        
        ## time complexity: O(n^2) where n is max of len(queries) and len(words)
        ## space complexity: O(n)