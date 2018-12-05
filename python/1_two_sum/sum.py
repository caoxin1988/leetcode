class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        
        for i in range(len(nums)):
            d[nums[i]] = i
            
        for i in range(len(nums)):
            data1 = nums[i]
            data2 = target - data1
            if data2 in d.keys() and d[data2] != i:
                return [i, d[data2]]
            
        return None