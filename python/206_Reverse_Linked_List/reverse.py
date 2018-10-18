class LinkNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverse(self, head):

        if head is None or head.next is None:
            return head

        ptr = head
        prev = None

        while ptr:
            next_ptr = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = next_ptr

        return prev

def transfer_link_list_to_string(head):
    
    result = ''
    while head:
        result += str(head.val) + ', '
        head = head.next

    return '[' + result[0:-2] + ']'

def transfer_to_linked_list(items):

    dummyptr = LinkNode(0)
    ptr = dummyptr
    
    for item in items:
        ptr.next = LinkNode(item)
        ptr = ptr.next

    ptr = dummyptr.next

    return ptr

def main():
    items = input('please input : ')

    head = transfer_to_linked_list(items)

    ret = Solution().reverse(head)

    out = transfer_link_list_to_string(ret)
    print(out)


if __name__ == '__main__':
    main()