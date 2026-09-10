"""
Accounts Merge
--------------
Each account is a list where the first element is a person's name and the
rest are email addresses belonging to that account. Two accounts belong to
the same real person if they share at least one email, even if the listed
names differ in casing or the accounts were entered separately. Merge all
accounts that refer to the same person and return, for each person, their
name followed by their sorted, deduplicated emails.

Time:  O(n * k * log(n * k)) where n is the number of accounts and k is the
       average number of emails per account, dominated by sorting the
       merged email lists (union-find operations are nearly O(1) amortized).
Space: O(n * k) for the union-find structure and email-to-account map.
"""

from typing import Dict, List


class UnionFind:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.parent[root_b] = root_a


def accounts_merge(accounts: List[List[str]]) -> List[List[str]]:
    uf = UnionFind(len(accounts))
    email_to_account: Dict[str, int] = {}

    for i, account in enumerate(accounts):
        for email in account[1:]:
            if email in email_to_account:
                uf.union(email_to_account[email], i)
            else:
                email_to_account[email] = i

    grouped: Dict[int, set] = {}
    for email, account_index in email_to_account.items():
        root = uf.find(account_index)
        grouped.setdefault(root, set()).add(email)

    merged = []
    for root, emails in grouped.items():
        name = accounts[root][0]
        merged.append([name] + sorted(emails))
    return merged


if __name__ == "__main__":
    accounts1 = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]
    print(sorted(map(sorted, accounts_merge(accounts1))))
    # expected output: [['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'], ['John', 'johnnybravo@mail.com'], ['Mary', 'mary@mail.com']]

    accounts2 = [["Alice", "a1@mail.com"], ["Bob", "b1@mail.com"]]
    print(sorted(map(sorted, accounts_merge(accounts2))))
    # expected output: [['Alice', 'a1@mail.com'], ['Bob', 'b1@mail.com']]

    accounts3 = [
        ["Kevin", "kevin1@mail.com", "kevin2@mail.com"],
        ["Kevin", "kevin2@mail.com", "kevin3@mail.com"],
        ["Kevin", "kevin3@mail.com", "kevin4@mail.com"],
    ]
    print(sorted(map(sorted, accounts_merge(accounts3))))
    # expected output: [['Kevin', 'kevin1@mail.com', 'kevin2@mail.com', 'kevin3@mail.com', 'kevin4@mail.com']]
