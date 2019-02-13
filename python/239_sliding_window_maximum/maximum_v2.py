from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        result = []
        deq = deque()

        if not nums:
            return result

        for i, val in enumerate(nums):
            if i >= k and deq[0] <= i -k:
                deq.popleft()
            
            # while deq:
            #     if nums[deq[-1]] <= val:
            #         deq.pop()
            #     else:
            #         break
            while deq and nums[deq[-1]] <= val:
                deq.pop()
            
            deq.append(i)

            if i >= k -1:
                result.append(nums[deq[0]])

        return result


# nums = [1,3,-1,-3,5,3,6,7]
# nums = [1,3,1,2,0,5]
nums = [9,10,9,-7,-4,-8,2,-6]
k = 5

solution = Solution()
print(solution.maxSlidingWindow(nums, k))