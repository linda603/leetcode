class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque()

        for i in range(1, n + 1):
            queue.append(i)
        # 1 2 3 4 5 , k = 2 -> next: 3 4 5 1 -> 5 1 3 - > 3 5 -> 3
        while len(queue) > 1:
            for i in range(k - 1):
                queue.append(queue.popleft())
            queue.popleft()

        return queue[0]

#Time: O(n * k)
#Space: O(n)