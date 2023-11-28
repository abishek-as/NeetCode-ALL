from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for e in emails:
            i, local = 0, ""
            while e[i] not in ["@", "+"]:
                if e[i] != ".":
                    local += e[i]
                i += 1

            while e[i] != "@":
                i += 1
            domain = e[i+1:]
            unique.add((local + domain))
        return len(unique)

    # # With in-built function
    # def numUniqueEmails(self, emails: list[str]) -> int:
    #     unique_emails: set[str] = set()
    #     for email in emails:
    #         local_name, domain_name = email.split('@')
    #         local_name = local_name.split('+')[0]
    #         local_name = local_name.replace('.', '')
    #         email = local_name + '@' + domain_name
    #         unique_emails.add(email)
    #     return len(unique_emails)


obj = Solution()
print(obj.numUniqueEmails(["test.email+alex@leetcode.com",
      "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]))
print(obj.numUniqueEmails(
    ["test.email+alex@leetcode.com", "test.email.leet+alex@code.com"]))
