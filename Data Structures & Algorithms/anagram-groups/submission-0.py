class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1 :
            return [strs]


        #segregation based on length
        from collections import defaultdict
        result = defaultdict(list)

        for word in strs:
            sor = "".join(sorted(word))
            result[sor].append(word)
        
        fr = list(result.values())

        
        return fr