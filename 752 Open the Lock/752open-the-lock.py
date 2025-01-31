class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def children(lock):
            res = []
            for i in range(4):
                x = int(lock[i])
                for diff in [-1, 1]:
                    digit = (x + diff + 10) % 10
                    curr_lock = lock[:i] + str(digit) + lock[i + 1:]
                    res.append(curr_lock)
            return res

        # BFS solution
        queue = collections.deque(["0000"])
        level = 0
        visited = set(deadends)

        if "0000" in visited: # "0000" is in deadends
            return -1
        
        visited.add("0000")

        while queue:
            size = len(queue)
            for i in range(size):
                lock = queue.popleft()
                if lock == target:
                    return level
                for child in children(lock):
                    if child not in visited:
                        queue.append(child)
                        visited.add(child)
            level += 1
        return -1

# Time: O(8*4 + 10^4 + d). d: len(deadends)
# There are 10^4 possiblities combinations.
# For each level, there are 8 possiblities of 1 lock + curr_lock takes O(4) -> O(8*4)
# O(d) to create visited set with deadends
#
# Space: O(10^4) queue + visited