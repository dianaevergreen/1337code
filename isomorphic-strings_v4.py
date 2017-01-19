class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        def iso(s,t):
            M={}
            for i in range(len(s)):
                x,y=s[i],t[i]
                if not x in M:
                    M[x] = y
                elif M[x] != y:
                    return False
            return True
        return iso(s, t) and iso(t, s)