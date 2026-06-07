class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # return sorted(s) == sorted(t)
        if len(s)!=len(t):
            return False
        from collections import defaultdict
        count = defaultdict(int)
        for ch in s:
            count[ch] += 1
        for ch in t:
            if ch not in count or count[ch] == 0:
                return False
            count[ch]-=1
        return True
        