class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0

        for string in logs:
            if string == "../":
                depth = max(0, depth - 1)
            elif string == "./":
                continue
            else:
                depth += 1
        return depth

#Time: O(n)
#Space: O(1)