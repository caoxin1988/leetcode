# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        ptr_a, ptr_b = headA, headB
        
        while ptr_a != ptr_b:
            print(ptr_a.val, ptr_b.val) 
            ptr_a = headB if ptr_a.next is None else ptr_a.next
            ptr_b = headA if ptr_b.next is None else ptr_b.next

        return ptr_a


a = [1, 2, 3, 15]
b = [11, 12, 13, 15]

lista = None
listb = None

dummp_ptr = ListNode(0)
ptr = dummp_ptr

for item in a:
    ptr.next = ListNode(item)
    ptr = ptr.next

lista = dummp_ptr.next
## =============

dummp_ptr = ListNode(0)
ptr = dummp_ptr

for item in b:
    ptr.next = ListNode(item)
    ptr = ptr.next

listb = dummp_ptr.next

solution = Solution()
m = solution.getIntersectionNode(lista, listb)

if m:
    print(m.val)
else:
    print('None')