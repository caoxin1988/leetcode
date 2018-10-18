class Solution(object):
    def hasCycle(self, head):
        fast_ptr = head.next
        slow_ptr = head

        while fast_ptr != slow_ptr:
            
            if fast_ptr is None or fast_ptr.next is None:
                return False
            
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next

        return True
