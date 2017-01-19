class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False

        dicty_s = {}
        
        for i in range(len(s)):
            if dicty_s.get(s[i]):
                if dicty_s[s[i]] != t[i]:
                    return False
            else:
                if t[i] not in dicty_s.values():
                    dicty_s[s[i]] = t[i]
                else:
                    return False
        return True
