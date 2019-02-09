import math

class Solution:
    def evalRPN(self, tokens):
        data = []

        opera = {'+', '-', '*', '/'}
        for item in tokens:
            if item in opera:
                if item == '+':
                    r = data.pop() + data.pop()
                    data.append(r)
                elif item == '-':
                    a, b = data.pop(), data.pop()
                    data.append(b - a)
                elif item == '*':
                    a, b = data.pop(), data.pop()
                    data.append(b * a)
                elif item == '/':
                    a, b = data.pop(), data.pop()
                    data.append(int(b /a))
            else:
                data.append(int(item))


        return data.pop()


solution = Solution()

nums = [['2','1','+','3','*'], ['4','13','5','/','+'],
    ['10','6','9','3','+','-11','*','/','*','17','+','5','+']]

for num in nums:
    print(solution.evalRPN(num))
