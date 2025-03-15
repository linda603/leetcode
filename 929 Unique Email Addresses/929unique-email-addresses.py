class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emails_set = set()

        for email in emails:
            local, domain = email.split("@")
            new_local = ""
            for c in local:
                if c == "+":
                    break
                if c == ".":
                    continue
                new_local += c
            emails_set.add(new_local + "@" + domain)
        return len(emails_set)

# Time: O(n)
# Space: O(n