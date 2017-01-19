class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        mitad = len(nums) / 2
        
        cant_nums = {}
        
        for n in nums:
            if n not in cant_nums:
                cant_nums[n] = 1
            else:
                cant_nums[n] += 1
                
                
        for k, v in cant_nums.items():
            if v > mitad:
                return k