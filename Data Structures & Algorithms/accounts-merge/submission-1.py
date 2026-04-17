class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        if len(accounts) == 1:
            entry = [accounts[0][0]]
            entry.extend(set(accounts[0][1:]))
            return [entry]

        # {email:account}
        email_owner = {}

        # 对所有email建无向图
        # {email:[other_email]}
        adj_table = defaultdict(set)
        for account in accounts:
            account_name = account[0]
            emails = account[1:]

            # 不要两两建边，会有O(n^2)复杂度
            email = emails[0]
            email_owner[email] = account_name

            for other_email in emails[1:]:
                adj_table[email].add(other_email)
                adj_table[other_email].add(email)
            

        visited = set()

        # dfs遍历图
        def dfs(email: str, all_emails: set[str]):

            for other_email in adj_table[email]:
                if other_email not in visited:
                    visited.add(other_email)

                    all_emails.add(other_email)
                    dfs(other_email, all_emails)
            
            return

        res = []
        for email in email_owner.keys():
            if email not in visited:
                visited.add(email)

                entry = [email_owner[email]]
                
                all_emails = set([email])
                dfs(email, all_emails)

                entry.extend(all_emails)
                
                res.append(entry)

        return res