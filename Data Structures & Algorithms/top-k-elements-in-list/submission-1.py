class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        freq_ = defaultdict(int)
        for i in nums:
            freq_[i]+=1
        #sort as per values
        sorted_items = sorted(freq_.items(),key = lambda item:item[1],reverse=True)
        return [item[0] for item in sorted_items[:k]]
        
        