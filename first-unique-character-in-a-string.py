class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        letters = {}
        
        for i in s:
            if letters.get(i):
                letters[i] += 1
            else:
                letters[i] = 1
                
        for k in range(len(s)):
            if letters[s[k]] == 1:
                return k
        return -1
            
        
       