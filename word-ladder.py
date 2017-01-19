class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        
        wordList.add(endWord) 
        
        Q = [[beginWord, 1]]
        marked = set([beginWord])
        
        
        while Q:
            current, level = Q.pop(0)
			
            for p in range(len(current)):
                #new_word = list(current)
                left = current[:p]
                right = current[p+1:]
                for l in range(26):
                    #new_word[p] = chr(l+97) 
                    #new_word = ''.join(new_word)
                    new_word = left + chr(l+97) + right
                    if new_word == endWord:
                        return level + 1
                    if new_word not in marked and new_word in wordList:
                        Q.append([new_word, level + 1])
                        marked.add(new_word)
                    #new_word = list(new_word)
		
        return 0
                    
                    
 
                    
                