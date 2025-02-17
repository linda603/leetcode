class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        adj = {}

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                if pattern not in adj:
                    adj[pattern] = []
                adj[pattern].append(word)
    
        queue = deque([beginWord])
        visited = set()

        count = 1
        while queue:
            size = len(queue)
            for i in range(size):
                word = queue.popleft()
                if word == endWord:
                    return count
                visited.add(word)
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for nei in adj[pattern]:
                        if nei not in visited:
                            queue.append(nei)
            count += 1
        return 0

# Time: O(nw*w + nw*w). O(nw) = len(wordList) = E + V
# Space: O(nw + nw)