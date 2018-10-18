
class ListNode(object):
    def __init__(self, x):
        self.x = x
        self.next = None


class Solution(object):
    def is_parlindrome(self, head):

        if head is None or head.next is None:
            return True
        
        fast_ptr = head
        slow_ptr = head
        prev = head
        
        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
                
            next_ptr = slow_ptr.next
            slow_ptr.next = prev
            prev = slow_ptr
            slow_ptr = next_ptr
            
            if fast_ptr and fast_ptr.next is None:
                slow_ptr = slow_ptr.next
                
        while slow_ptr:
            if slow_ptr.val != prev.val:
                return False
            
            slow_ptr = slow_ptr.next
            prev = prev.next
            
        return True


def transfer_to_listnode(items):
    dummyptr = ListNode(0)
    ptr = dummyptr

    for item in items:
        ptr.next = ListNode(item)
        ptr = ptr.next

    ptr = dummyptr.next

    return ptr


def main():
    lis = input("please input:")
    head = transfer_to_listnode(lis)

    ptr = head
    while ptr is not None:
        print('dacaoxin', ptr.x)
        ptr = ptr.next


    ret = Solution().is_parlindrome(head)
    print(ret)


if __name__ == '__main__':
    main()