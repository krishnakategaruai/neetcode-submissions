class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = list(set(nums))

        if len(nums) == 1:
            return 1
        if len(nums) == 0:
            return 0
        

        nums.sort()

        i = 0 

        result = set()

        max = 1

        

        while(i<len(nums)-1):

        
            if nums[i+1] - nums[i] == 1:
                result.add(i)
                result.add(i+1)
            else:
                result = set()
            if max < len(result):
                max = len(result)

                
            # print(nums[i],nums[i+1],max,result)
            i+=1



        return max