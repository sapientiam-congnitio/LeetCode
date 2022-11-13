class Solution(object):
    def kWeakestRows(self, mat, k):
        strength = []
        final = []
        for i in mat:
            strength.append(i.count(1))
        stats = list(enumerate(strength))
        ensort = sorted(stats, key=lambda x:x[1])
        for i in range(k):
            final.append(ensort[i][0])
        return final