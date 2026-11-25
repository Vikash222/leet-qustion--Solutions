class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n, M1, M2, B1, B2 = len(nums), 10**9+7, 10**9+9, 131542391, 265443576
        p1, p2, h1, h2 = [1]*(n+1), [1]*(n+1), [0]*(n+1), [0]*(n+1)
        for i, x in enumerate(nums):
            p1[i+1], p2[i+1] = p1[i]*B1%M1, p2[i]*B2%M2
            h1[i+1], h2[i+1] = (h1[i]*B1+x)%M1, (h2[i]*B2+x)%M2
        lo, hi = 1, n
        while lo < hi:
            m = (lo+hi)//2; w1, w2, s = p1[m], p2[m], {}
            for i in range(n-m+1): k = (((h1[i+m]-h1[i]*w1)%M1)<<30)|((h2[i+m]-h2[i]*w2)%M2); s[k] = 2 if k in s else 1
            ok = 1 in s.values(); hi, lo = (m, lo) if ok else (hi, m+1)
        return lo