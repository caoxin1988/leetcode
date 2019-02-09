import math

class Solution:
    def myAtoi(self, str):
        result = 0

        i, N, former = 0, len(str), 1

        while i < N:
            if str[i] != ' ':
                break        
            i += 1
            
        if i < N and (str[i] == '-' or str[i] == '+'):
            former = -1 if str[i] == '-' else 1
            i += 1
            
        while i < N:
            if str[i].isdigit():
                result = result * 10 + int(str[i])
                i += 1
            else:
                break

        result = result * former
        if result > (math.pow(2, 31) * -1) and result < (math.pow(2,31) - 1):
            return result
        elif former > 0 :
            return int(math.pow(2,31) - 1)
        else:
            return int(math.pow(2,31) * -1)
        # return max(int(math.pow(2, 31) * -1), min(result, int(math.pow(2,31) - 1)))

solution = Solution()

s = ['42', '-42', '4193 with words', 'words and 987', '-91283472332']
for sub in s:
    print(solution.myAtoi(sub))