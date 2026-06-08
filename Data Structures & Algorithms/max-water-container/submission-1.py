class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #i-j *  height()

        i ,j = 0,len(heights)-1
        max = 0
        while(i<j):
            height = min(heights[i],heights[j])
            width = j-i

            if height*width > max :
                max = height*width
            
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return max
        