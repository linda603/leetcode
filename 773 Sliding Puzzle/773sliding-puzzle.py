class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        adj = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        target = "123450"
        source = "".join([str(board[r][c]) for r in range(2) for c in range(3)])
        queue = deque([source])
        visited = set([source])

        swaps = 0
        while queue:
            size = len(queue)
            for i in range(size):
                curr_str = queue.popleft()
                if curr_str == target:
                    return swaps
                curr_arr = list(curr_str)
                zero_idx = curr_arr.index("0")
                for nei in adj[zero_idx]:
                    tmp = list(curr_str)
                    tmp[nei], tmp[zero_idx] = tmp[zero_idx], tmp[nei]
                    nei_str = "".join(tmp)
                    if nei_str not in visited:
                        queue.append(nei_str)
                        visited.add(nei_str)
            swaps += 1
        return -1

# Time: O(mn!*mn). O(mn!) permutation for queue. O(mn) to look for index "0"
# Space: O(mn!) for queue + set. O(mn) for curr_arr, tmp arr