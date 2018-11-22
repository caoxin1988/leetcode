class Solution(object):
    def majority_element(self, nums):
        count = len(nums)//2
        result = {}

        for num in nums:
            if str(num) in result.keys():
                result[str(num)] += 1
            else:
                result[str(num)] = 1
            
        for key in result.keys():
            if result[key] > count:
                return int(key)