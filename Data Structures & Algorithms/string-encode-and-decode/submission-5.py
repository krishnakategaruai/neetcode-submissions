class Solution:

    def encode(self, strs: List[str]) -> str:

       result = ""
       for i in strs:
           result += "#" + str(len(i))+"#"+i
       print(result)
       return result


    def decode(self, s: str) -> List[str]:
        
        result = []
        i = 0
        while(i<len(s)):

            if s[i] == "#":
                j = i+1
                while(j!="#"):
                    if s[j] == "#":
                        break
                    j +=1

                length = int(s[i+1:j])
                word = s[j+1 : j+1 +length]
                result.append(word)
        
            i  = j+1 + length
           


        print(result)
        return result

