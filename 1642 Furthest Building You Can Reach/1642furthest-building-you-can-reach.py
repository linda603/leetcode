class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = [] # max heap to store the diff that already used bricks to move

        for i in range(len(heights) - 1):
            if heights[i + 1] <= heights[i]:
                continue
            diff = heights[i + 1] - heights[i]
            heapq.heappush(heap, -diff)
            bricks -= diff

            if bricks < 0: # not able to move to i + 1 by using bricks
                if ladders == 0:
                    return i
                ladders -= 1
                # max diff in heap will use ladder instead of bricks
                prev_diff = -(heapq.heappop(heap))
                bricks += prev_diff
        return len(heights) - 1

# Time: O(nlogn)
# Space: O(n)