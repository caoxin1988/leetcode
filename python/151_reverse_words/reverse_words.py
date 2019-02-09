class Solution:
    def reverseWords(self, s):
        s = s.strip()
        s = s.split(' ')

        print(s)

        return ' '.join(s[::-1])

s = '  a  b '
solution = Solution()
print(solution.reverseWords(s))
print('b a')
print('b  a')