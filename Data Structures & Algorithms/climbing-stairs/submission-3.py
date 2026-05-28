class Solution:
    def climbStairs(self, n: int) -> int:

        f_1 = 1
        f_2 = 2

        if n < 3:
            return n

        #fn = fn-1,fn-2
        
        for _ in range(3,n+1):

            temp = f_1 + f_2
            f_1 = f_2
            f_2 = temp



        return temp

        


        