from collections import defaultdict

class Solution(object):
    def majority_element(self, nums):
        count = len(nums)//2
        result = defaultdict(int)

        for num in nums:
                result[num] += 1
            
        for key in result.keys():
            if result[key] > count:
                return int(key)