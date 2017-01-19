class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
       
        if len(nums) == 1:
            return nums[0]
        
        tmp = nums[0]
        for n in nums[1:]:
            if tmp > n:
                return n
        return tmp
            