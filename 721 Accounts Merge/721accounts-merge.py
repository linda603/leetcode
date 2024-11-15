class union_find:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find_par(self, i):
        p = self.parent[i]

        while p != self.parent[p]:
            p = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    
    def union(self, i1, i2):
        p1 = self.find_par(i1)
        p2 = self.find_par(i2)

        if p1 == p2:
            return False
        if self.rank[p1] >= self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        union_f = union_find(n)

        email_to_i = {} # map email to account idx
        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email not in email_to_i:
                    email_to_i[email] = i
                else:
                    union_f.union(email_to_i[email], i)
        
        i_to_email = defaultdict(list)
        for email, i in email_to_i.items():
            parent_i = union_f.find_par(i)
            i_to_email[parent_i].append(email)
        
        res = []
        for i, emails in i_to_email.items():
            name = accounts[i][0]
            res.append([name] + sorted(emails))
        return res

# Time: O(nl*n + nl + nllognl). n: len(accounts), l: longest length of an account
# Space: O(nl)