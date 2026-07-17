class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            res += self.countPali(s, i, i)
            res += self.countPali(s, i, i+1)

        return res

    def countPali(self, st, l, r):
        res = 0

        while l >= 0 and r < len(st) and st[l] == st[r]:
            res += 1
            l -= 1
            r += 1
        return res
            