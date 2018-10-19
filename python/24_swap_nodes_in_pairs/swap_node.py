
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swap(self, head : ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        head_new = head.next
        prev = None
        first = head
        second = head.next

        while second:
            first1 = first
            second1 = second

            first = first.next.next
            if second.next is not None:
                second = second.next.next
            else:
                second = None

            if prev:
                prev.next = second1
                second1.next = first1
                prev = first1
            else:
                second1.next = first1
                prev = first1
        else:
            if first is None:
                prev.next = None
            else:
                prev.next = first
                first.next = None

        return head_new


def transfer_string_to_list(items) -> ListNode:
    dummy = ListNode(0)
    ptr = dummy

    for item in items:
        ptr.next = ListNode(item)
        ptr = ptr.next

    return dummy.next

def transfer_list_to_string(head : ListNode):

    if head is None:
        return '[]'

    string = ''
    while head:
        string += head.val + ', '
        head = head.next

    return '[' + string[:-2] + ']'

def main():
    items = input('please input : ')
    head = transfer_string_to_list(items)
    lis = Solution().swap(head)

    ret = transfer_list_to_string(lis)
    print(ret)

if __name__ == '__main__':
    main()