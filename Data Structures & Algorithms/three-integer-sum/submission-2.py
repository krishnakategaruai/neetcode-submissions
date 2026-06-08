class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        i = 0
 
        result = []

        while(i<len(nums)):
            val = nums[i]
            j = i+1
            k = len(nums)-1



            while(j<k):

                if nums[j] + nums[k] == -val:
                    result.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    

                
                elif nums[j] + nums[k] > -val : 
                    k -= 1
                else:
                    j += 1
            i += 1
            
        return list(set(( tuple(x) for x in result)))




                

        