import time

def cal_time(func):
    def wrapper(*args, **argdict):
        start = time.time()
        res = func(*args, **argdict)
        print(time.time() - start)

        return res

    return wrapper

@cal_time
def cal_stairs():
    solution = Solution()
    print(solution.climbStairs(44))

class Solution:
    def __init__(self):
        self.buf = {1:1, 2:2}

    def climbStairs(self, n):

        if n in self.buf:
            return self.buf[n]

        res = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.buf[n] = res

        return res
        

cal_stairs()