class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0] * n

        moves = 0
        total_balls = 0
        for i in range(n):
            moves = total_balls + moves
            res[i] = moves
            total_balls += int(boxes[i])
        
        moves = 0
        total_balls = 0
        for i in range(n - 1, -1, -1):
            moves = total_balls + moves
            res[i] += moves
            total_balls += int(boxes[i])
        return res

# Time: O(2n)
# Space: O(1)