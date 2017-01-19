class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < s or not nums:
            return 0

                
        start = end = 0
        L = len(nums)
        SUM = 0
        res = L
      
        while SUM <= s and end < L:
            SUM += nums[end]
            end += 1
          
            while SUM >= s and start < end:
                SUM -= nums[start]
                start += 1
              
                if end -start + 1 < res:
                    res = end -start + 1
         
        return res               
              
                
                