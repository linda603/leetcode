class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gapCount = {0: 0} # position: gaps

        for row in wall:
            pos = 0
            for bricks in row[:-1]:
                pos = pos + bricks
                if pos not in gapCount:
                    gapCount[pos] = 0
                gapCount[pos] += 1
        
        maxGaps = max(gapCount.values())
        return len(wall) - maxGaps

#Time: O(n) n: total bricks in a wall
#Space: O(m) m entries, where m refers to the width of the wall