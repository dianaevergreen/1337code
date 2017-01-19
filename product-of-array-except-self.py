class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = 1
        Flag = False
        cero_counters = 0
        
        for n in nums:
            if n != 0:
                total *= n
            else:
                Flag = True
                cero_counters += 1
        
        if Flag is False:
            array = []
            for n in range(len(nums)):
                array.append(total/nums[n])
        else:
            if cero_counters == 2:
                array=[0]* (len(nums))
                return array
            else:
                i = nums.index(0)
                array = [0]*(len(nums))
                multiplier = 1
                
                for x in range(len(nums)):
                    if x != i:
                        multiplier *= nums[x]
                        
                array[i] = multiplier
                        
                        
            
        return array
            
     