class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        t = ""
        for i in s:
            if i.isalpha() or i.isnumeric():
                t += i.lower()
                
                
        print(t)
        if t == t[::-1]:
            return True
        return False
        