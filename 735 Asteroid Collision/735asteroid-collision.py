class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            while stack and stack[-1] > 0 and ast < 0:
                if stack[-1] == -ast:
                    stack.pop()
                    break
                elif stack[-1] < -ast:
                    stack.pop()
                else:
                    break
            else:
                stack.append(ast)
        return stack

# Time: O(n)
# Space: O(n)