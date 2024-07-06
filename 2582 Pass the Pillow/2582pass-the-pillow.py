class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        fullRounds = time // (n - 1)
        remain = time % (n - 1)

        # If fullRounds is even, the pillow is moving forward
        if fullRounds % 2 == 0:
            return remain + 1 #Position when moving forward
        # If fullRound is odd, the pillow is moving backward
        else:
            return n - remain #Position when moving backward

#Time: O(1)
#Space: O(1)