from collections import Counter

class Solution:
    def isAnagram(self, s: 'str', t: 'str') -> 'bool':
        dict1, dict2 = Counter(s), Counter(t)
        
        return dict1 == dict2