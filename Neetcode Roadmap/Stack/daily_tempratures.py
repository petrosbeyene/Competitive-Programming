class Solution:
    def dailyTemperatures(self, temperatures):
        monotonic_stack = []
        answer = [0] * len(temperatures)
        for i, val in enumerate(temperatures):
            while monotonic_stack and val > temperatures[monotonic_stack[-1]]:
                curr = monotonic_stack.pop()
                answer[curr] = i - curr

            monotonic_stack.append(i)
        
        return answer

        #Time complexity = O(N) -> worst case scenario = Amortized time complexity
        #Space complexity = O(N)

                
