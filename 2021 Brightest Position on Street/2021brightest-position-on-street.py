class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        spots = defaultdict(int)

        for pos, dist in lights:
            spots[pos - dist] += 1
            spots[pos + dist + 1] -= 1

        count = 0
        brightest = 0
        res = 0
        for pos, val in sorted(spots.items()):
            count += val
            if count > brightest:
                brightest = count
                res = pos
        return res

# Time: O(n + nlogn) due to sorting
# Space: O(n)