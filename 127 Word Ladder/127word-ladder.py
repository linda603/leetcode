class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        adj = {} # pattern: [list of words]
                 # *og: [cog, log, dog]

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                if pattern not in adj:
                    adj[pattern] = []
                adj[pattern].append(word)
        
        # BFS solution
        queue = collections.deque([beginWord])
        visited = set([beginWord])
        res = 1

        while queue:
            size = len(queue)
            for i in range(size):
                word = queue.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for nei in adj[pattern]:
                        if nei not in visited:
                            queue.append(nei)
                            visited.add(nei)
            res += 1
        
        return 0

# Time: (n*w*w + n*w*w). n: len(wordList), w: len(longestWord)
# Space: O(n*w) for adj hash map