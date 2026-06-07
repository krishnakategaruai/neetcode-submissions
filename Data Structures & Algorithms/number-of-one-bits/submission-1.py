class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        if n==0:
            return 0
        for i in range(1,33):
            n = n & (n-1)
            if n:
                continue
            else:
                return i
        return 0

            