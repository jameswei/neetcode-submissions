class UnionFind:
    def __init__(self):
        self.parents = {}

    def find(self, val: str) -> str:
        if self.parents[val] != val:
            # 通过直接更新最终的父节点来实现“路径压缩”
            self.parents[val] = self.find(self.parents[val])
        
        return self.parents[val]
    
    def union(self, val_1: str, val_2: str):
        if val_1 not in self.parents:
            self.parents[val_1] = val_1
        if val_2 not in self.parents:
            self.parents[val_2] = val_2
        
        parent_1 = self.find(val_1)
        parent_2 = self.find(val_2)

        if parent_1 != parent_2:
            # 还可以按秩优化
            self.parents[parent_2] = parent_1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # union-find解法和dfs不同的是，它不需要预先存在的静态图，它更适合于动态**合并**集合（动态得隐式得连通）
        # 对于数据规模大或者是流式数据（无法静态获取全部），union-find时间和空间复杂度都更高效
        email_to_owner = {}
        union_find = UnionFind()

        for account in accounts:
            name = account[0]
            email = account[1]

            email_to_owner[email] = name

            for other_email in account[1:]:
                email_to_owner[other_email] = name
                union_find.union(email, other_email)

        email_groups = defaultdict(set)

        for email in email_to_owner.keys():
            email_groups[union_find.find(email)].add(email)

        res = []

        for k, v in email_groups.items():
            entry = [email_to_owner[k]]
            emails = list(v)
            emails.sort()
            entry.extend(emails)
            res.append(entry)

        return res
