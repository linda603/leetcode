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
        queue = collections.deque([source])
        visited = set([source])

        move = 0
        while queue:
            size = len(queue)
            for i in range(size):
                curr_str = queue.popleft()
                if curr_str == target:
                    return move
                curr_arr = list(curr_str)
                zero_idx = curr_arr.index("0") 
                for nei in adj[zero_idx]:
                    tmp = curr_arr.copy()
                    tmp[nei], tmp[zero_idx] = tmp[zero_idx], tmp[nei]
                    nxt = "".join(tmp)
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)
            move += 1
        
        return -1

# Time: O(mn!*mn). queue takes O(mn!) for all permutation. O(mn) to look through the string to find zero index
# Space: O(mn!). visited set() takes O(mn!), queue takes O(mn!)