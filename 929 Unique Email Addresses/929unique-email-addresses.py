class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        addresses = set()

        for email in emails:
            local, domain = email.split("@")
            updated_local = ""
            for c in local:
                if c == ".":
                    continue
                elif c == "+":
                    break
                updated_local += c
            addresses.add(updated_local + "@" + domain)
        return len(addresses)

# Time: O(n*(l + l)) = O(nl). n: len(emails), l: len(string email)
# Space: O(nl)