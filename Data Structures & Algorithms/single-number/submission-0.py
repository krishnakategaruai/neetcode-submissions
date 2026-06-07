class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from functools import reduce
        import operator
        return reduce(operator.xor, nums)
        