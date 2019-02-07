class Solution:
    def threeSumCloset(self, nums, target):
        nums.sort()
        N = len(nums)
        min_diff = abs(target - nums[0] - nums[1] - nums[N-1])
        result = nums[0] + nums[1] + nums[N-1]

        for i in range(N):
            s, e = i+1, N-1

            t = target - nums[i]
            while s < e:
                if abs( target - nums[i] - nums[e] - nums[s]) < min_diff:
                    min_diff = abs( target - nums[i] - nums[e] - nums[s])
                    result = nums[i] + nums[e] + nums[s]
                    
                if nums[s] + nums[e] < t:
                    s += 1
                else:
                    e -= 1

        return result


nums = [-1, 2, 1, -4]
target = 1

solution = Solution()
result = solution.threeSumCloset(nums, target)

print(result)