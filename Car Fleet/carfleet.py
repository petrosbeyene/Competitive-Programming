class Solution:
    def carFleet(self, target: int, position, speed) -> int:
        stack = []
        for pos, vel in sorted(zip(position, speed))[::-1]:
            dist = target - pos
            arr_time = dist/vel
            if not stack:
                stack.append(arr_time)
            if arr_time > stack[-1]:
                stack.append(arr_time)
        return len(stack)