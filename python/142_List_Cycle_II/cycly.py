class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        slow = head
        fast = head
        
        while fast and fast.next:
            
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                fast = head
                break
        else:
            return None
        
        while fast != slow:
            fast = fast.next
            slow = slow.next
            
        return fast