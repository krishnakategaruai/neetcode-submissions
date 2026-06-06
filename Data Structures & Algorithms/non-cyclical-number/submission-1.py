class Solution:
    def isHappy(self, n: int) -> bool:
        num_list = list(str(n))
        
        def get_sum(num_list):
            sum = 0 
            for i in num_list:
                sum += int(i)**2
            return sum 
        
        visited_sum =set()
        sum = get_sum(num_list)
        while( sum not in visited_sum):
            if sum == 1 :
                return True
            else:
                visited_sum.add(sum)
                num_list = list(str(sum))
                sum = get_sum(num_list)
        return False



        