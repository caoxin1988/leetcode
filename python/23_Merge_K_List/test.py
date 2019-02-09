class ListNode:
    def __init__(self, x):
        self.val = x

a = (1, ListNode(1))
b = (1, ListNode(10))

print(a > b)