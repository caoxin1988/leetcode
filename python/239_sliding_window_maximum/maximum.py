from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        result = []
        deq = deque()

        if not nums:
            return result
        
        for i in range(k):
            while len(deq) != 0:
                if nums[deq[-1]] <= nums[i]:
                    deq.pop()
                else:
                    break

            deq.append(i)

        result.append(nums[deq[0]])

        for i in range(k, len(nums)):
            if deq[0] <= i - k:
                deq.popleft()

            while len(deq) != 0:
                if nums[deq[-1]] <= nums[i]:
                    deq.pop()
                else:
                    break

            deq.append(i)
            result.append(nums[deq[0]])

        return result


# nums = [1,3,-1,-3,5,3,6,7]
# nums = [1,3,1,2,0,5]
nums = [9,10,9,-7,-4,-8,2,-6]
k = 5

solution = Solution()
print(solution.maxSlidingWindow(nums, k))