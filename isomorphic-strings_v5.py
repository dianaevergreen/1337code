class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
            
        def iso(a,b):
            D = {}
            
            for x in range(len(a)):
                if a[x] not in D:
                    D[a[x]] = b[x]
                else:
                    if D[a[x]] != b[x]:
                        return False
            return True
            
        return iso(s,t) and iso(t,s)
   