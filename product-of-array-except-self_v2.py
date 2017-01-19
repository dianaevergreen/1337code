class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
       
        LM = [1]
        RM = [1]
        answer = []
        
        
        #Left Multiplicacion
        
        for n in range(1,len(nums)):
            LM.append(LM[-1]*nums[n-1])
            
        for m in range(len(nums)-2,-1,-1):
            RM.insert(0,nums[m+1]*RM[0])
            
        
        for nm in range(len(nums)):
            answer.append(LM[nm]*RM[nm])
        return answer
     