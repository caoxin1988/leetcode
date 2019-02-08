class Solution:
    def mysqrt(self, x):

        if x == 0:
            return 0

        left, right = 1, x

        while True:
            mid = (left + right) // 2

            if mid * mid > x:
                right = mid
            else:
                if (mid + 1) * (mid +1) > x:
                    return mid
                left = mid


x = 3

solution = Solution()
print(solution.mysqrt(x))