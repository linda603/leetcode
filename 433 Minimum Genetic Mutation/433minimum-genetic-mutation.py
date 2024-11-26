class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        
        queue = collections.deque([startGene])
        visited = set([startGene])

        def neighbor(a, b):
            cnt = 0

            for i in range(len(a)):
                if a[i] != b[i]:
                    cnt += 1
            return True if cnt == 1 else False

        res = 0
        while queue:
            # use for loop to check all curr nodes in queue
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                if curr == endGene:
                    return res
                for nei in bank:
                    if neighbor(curr, nei) and nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
            res += 1
        return -1

# Time: O(n^2*l)
# Space: O(nl + nl) for queue + visited