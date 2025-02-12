class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        res = [-1] * len(queries)

        for i in range(len(queries)):
            a, b = sorted(queries[i])
            if a == b or heights[a] < heights[b]:
                res[i] = b
                continue
            for j in range(b + 1, len(heights)):
                if heights[j] > heights[a] and heights[j] > heights[b]:
                    res[i] = j
                    break
        return res

# Time: O(q*n)
# Space: O(n)