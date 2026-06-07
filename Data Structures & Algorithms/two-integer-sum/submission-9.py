class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic_ = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in dic_:
                return [dic_[diff],i]
            
            dic_[n] = i
            
        