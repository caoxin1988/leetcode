class Solution:
    def firstMissingPositive(self, nums):
        result = min = 1

        nums.sort()
        for num in nums:
            if num == result:
                result += 1
        return result

nums = [[1,2,0], [3,4,-1,1], [7,8,9,11,12], [2,1]]

solution = Solution()

for num in nums:
    print(solution.firstMissingPositive(num))