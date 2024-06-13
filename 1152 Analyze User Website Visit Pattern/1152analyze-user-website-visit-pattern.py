from itertools import combinations
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        webInfo = {}

        for t, user, web in sorted(zip(timestamp, username, website)):
            if user not in webInfo:
                webInfo[user] = []
            webInfo[user].append(web)
        scores = {}
        #worst case all web is under 1 name => Time: O(n^3)
        for user, webs in webInfo.items():
            combi = self.getCombinations(webs, 3)
            for pattern in set(combi): #can use: for pattern in combinations(webs, 3)
                if pattern not in scores:
                    scores[pattern] = 0
                scores[pattern] += 1
        
        res = []
        maxScore = 0
        for pattern, score in scores.items():
            if (score > maxScore) or (score == maxScore and pattern < res):
                res = pattern
                maxScore = score
        
        return res


    def getCombinations(self, webs, n):
        if n == 0:
            return [[]]
        
        res = []
        for i in range(len(webs)):
            word = webs[i]
            remain = webs[i + 1:]

            remainList = self.getCombinations(remain, n - 1)
            for remainWords in remainList:
                res.append(tuple([word, *remainWords]))
        return tuple(res)

#Time: O(nlogn) + O(n^3) = O(n^3)
#Space: O(n^3)
