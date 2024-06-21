class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        queue = deque(range(0, len(deck)))
        res = [0] * len(deck)

        for num in deck:
            i = queue.popleft()
            res[i] = num
            if queue:
                j = queue.popleft()
                queue.append(j)

        return res

#Time: O(nlogn + n) sorting + iterate all deck
#Space: O(n) due to queue size.