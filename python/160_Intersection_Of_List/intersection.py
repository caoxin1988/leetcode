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
        count = 0
        
        while count <= 2:
            if ptr_a.val == ptr_b.val:
                return ptr_a
            
            ptr_a, ptr_b = ptr_a.next, ptr_b.next

            if not ptr_a:
                ptr_a = headB
                count += 1
                
            if not ptr_b:
                ptr_b = headA
                count += 1
        else:
            return None


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