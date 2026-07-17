class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()

        for email in emails:
            email = re.sub(r'\.(.+@)','$1', email)
            email = re.sub(r'\+.+?@', '', email)
            res.add(email)

        return len(res)  