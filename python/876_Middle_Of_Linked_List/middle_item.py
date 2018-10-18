
class LinkNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def middle_item(self, head):

        if head is None or head.next is None:
            return head
        
        fast_ptr = head
        slow_ptr = head

        while fast_ptr and fast_ptr.next:

            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next

        return slow_ptr

def transfor_link_list_to_string(head):

    if head is None:
        return '[]'

    string = ''

    while head:
        string = string + str(head.val) + ', '
        head = head.next

    return '[' + string[:-2] + ']'

def transfor_string_to_list(items):
    dummy_ptr = LinkNode(0)
    ptr = dummy_ptr

    for item in items:
        ptr.next = LinkNode(item)
        ptr = ptr.next

    ptr = dummy_ptr.next

    return ptr

def main():
    items = input('please input : ')

    head = transfor_string_to_list(items)

    ptr = Solution().middle_item(head)

    ret = transfor_link_list_to_string(ptr)

    print(ret)

if __name__ == '__main__':
    main()