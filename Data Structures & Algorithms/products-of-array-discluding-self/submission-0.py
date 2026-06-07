class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = 1
        prefix_ = []

        for i in range(len(nums)):
            prefix_.append(prefix)
            prefix *= nums[i]
        
        suffix = 1
        suffix_ = []
         
        for i in range(len(nums)-1,-1,-1):
            suffix_.append(suffix)
            suffix *= nums[i]

        result = []
        suffix_.reverse()
        for i,j in zip(prefix_,suffix_):
            result.append(i*j)
        
        return result

        
        