class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        
        dict_s ={}
        dict_t={}
        
        for i in range(len(s)):
            if dict_s.get(s[i]):
                dict_s[s[i]].append(i)
            else:
                dict_s[s[i]] = [i]
                
            if dict_t.get(t[i]):
                dict_t[t[i]].append(i)
            else:
                dict_t[t[i]] = [i]
                

        for i in range(len(s)):
            if dict_s[s[i]] != dict_t[t[i]]:
                return False
        return True
            