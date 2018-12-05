class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        
        for i in range(len(nums)):
            
            data = target - nums[i]
            
            if data in d.keys():
                return [d[data], i]
            else:
                d[nums[i]] = i
                
        return None