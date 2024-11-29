class Solution:
    def candy(self, ratings: List[int]) -> int:
        rewards = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                rewards[i] = rewards[i - 1] + 1
        
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and rewards[i] <= rewards[i + 1]:
                rewards[i] = rewards[i + 1] + 1

        return sum(rewards)

# Time: O(3n)
# Space: O(n)