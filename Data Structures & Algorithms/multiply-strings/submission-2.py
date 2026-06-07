class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) > 200 or len(num2)>200 or len(num1)<1 or len(num2)<0:
            return 0
        if num1 == "0" or num2 == "0":
            return "0"
        if num1=="1":
            return num2
        elif num2 =="1":
            return num1
        result = [0]*(len(num2)+len(num1))
        for i in range(len(num2)-1,-1,-1):
            for j in range(len(num1)-1,-1,-1):
                multiply = int(num1[j])*int(num2[i])

                total = result[i+j+1] + multiply
                result[i+j] += total//10
                result[i+j+1] = total%10


        return "".join(map(str,result)).lstrip("0")


    