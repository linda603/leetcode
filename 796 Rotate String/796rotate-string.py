class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        n = len(goal)
        double_string = s + s

        for i in range(len(double_string)):
            if double_string[i: i + n] == goal:
                return True
        return False

# Time: O(2n)
# Space: O(n)