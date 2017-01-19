class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dicty = {}
        
        for i in range(len(s)):
            if dicty.get(s[i]):
                if dicty[s[i]] != t[i]:
                    return False
            else:
                if t[i] not in dicty.values():
                    dicty[s[i]] = t[i]
                else:
                    return False
        return True