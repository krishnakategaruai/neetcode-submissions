class WordDictionary:

    def __init__(self):
        self.dictionary = []
        

    def addWord(self, word: str) -> None:
        if word.islower() and len(word)<=20:
            self.dictionary.append(word)

            

        

    def search(self, word: str) -> bool:
        if len(word)>=1 or len(word)<=20:

            if  not word.islower():
                if "." not in word:
                    return False
        else:
            return False
        word_match = None
        for w in self.dictionary:
            if len(w)!=len(word):
                continue
            else:
                for i,ch in enumerate(word):
                    word_match = True
                    if ch == ".":
                        continue
                    elif ch!=w[i]:
                        word_match = False
                        break
                if word_match:
                    return True
        return False

            
                    
        
