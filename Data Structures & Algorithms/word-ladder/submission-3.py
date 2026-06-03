class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if len(beginWord) < 1 or len(beginWord) > 10 or len(wordList) >100 :
            return 0

        if endWord not in wordList:
            return 0
        visited = set()
        
        from collections import deque,defaultdict
        adj_ = deque()

        adj_.append((beginWord,1))
        word_map = defaultdict(list)

        for currentword in wordList:
           for i in range(len(currentword)):
                regex = currentword[:i]+"*"+currentword[i+1:]
                word_map[regex].append(currentword)
        count = 0
        while(adj_):
            (currentword,step) = adj_.popleft()
            if currentword not in visited:
                if currentword == endWord:
                    return step
                for i in range(len(currentword)):
                    regex = currentword[:i]+"*"+currentword[i+1:]
                    if regex in word_map:
                        matched_words = word_map[regex]
                    else:
                        continue
                    for match in matched_words:
                        if match not in visited:
                            adj_.append((match,step+1))
                visited.add(currentword)
        return 0

                


                



                






       
        
        
        