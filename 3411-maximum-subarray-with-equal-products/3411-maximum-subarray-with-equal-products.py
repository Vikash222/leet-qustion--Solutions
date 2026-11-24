import math

class Solution(object):
    def maxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0

        for i in range(n):
            prod = 1
            g = 0
            l = 1
            for j in range(i, n):
                x = nums[j]
                prod *= x
                g = x if j == i else math.gcd(g, x)
                l = math.lcm(l, x)

                if prod == l * g:
                    ans = max(ans, j - i + 1)

        return ans