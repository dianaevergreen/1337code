class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1 or n== 2 or n==3:
            return True
        else:
            return bool(n%4)
        