class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        ht1 = {}
        ht2 = {}
        
        for i in s:
            if i not in ht1:
                ht1[i] = 1
                
            else:
                ht1[i] += 1
                
                
        for i in t:
            if i not in ht2:
                ht2[i] = 1
            else:
                ht2[i] += 1
                
        k1 = ht1.keys()
        k2 = ht2.keys()
        
        if k1 != k2:
            return False
        
        for x in k1:
            if ht1[x] != ht2[x]:
                return False
                
        return True
            