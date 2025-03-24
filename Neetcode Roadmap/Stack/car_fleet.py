class Solution:
    def carFleet(self, target: int, position, speed) -> int:
        pos_speed = list(zip(position, speed))
        pos_speed.sort(key=lambda x: x[0], reverse=True)

        time_monotonic_stack = []
        fleet = 0
        for ps_tuple in pos_speed:
            time = (target - ps_tuple[0]) / ps_tuple[1]
            if not time_monotonic_stack or time > time_monotonic_stack[-1]:
                fleet += 1
                time_monotonic_stack.append(time)
            
        
        return fleet

        #Time complexity = O(N)
        #Space complexity = O(N)
