class Solution:
    def reverseString(self, s: 'List[str]') -> 'None':
        """
        Do not return anything, modify s in-place instead.
        """
        i, N = 0, len(s)
        while i < N//2:
            s[i], s[N-1-i] = s[N-1-i], s[i]
            i += 1
            
        print(s)