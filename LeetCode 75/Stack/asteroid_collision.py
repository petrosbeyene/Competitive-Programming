class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        for asteroid in asteroids:
            while stack and (asteroid < 0 and stack[-1] > 0):
                curr = stack.pop()
                if abs(curr) > abs(asteroid):
                    asteroid = curr
                elif abs(asteroid) == abs(curr):
                    asteroid = 0
            
            if asteroid != 0:
                stack.append(asteroid)

        return stack

        # Time complexity: O(N)
        # Space complexity: O(N)