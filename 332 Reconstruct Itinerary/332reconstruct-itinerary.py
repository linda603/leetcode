class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        adj = {src: [] for src, des in tickets}

        for src, des in tickets:
            adj[src].append(des)

        res = []
        stack = ["JFK"]

        while stack:
            while stack[-1] in adj and adj[stack[-1]]:
                stack.append(adj[stack[-1]].pop())
            res.append(stack.pop())
        
        return res[::-1]

#Time: O(E + V)
#Space: O(E + V)