
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swap(self, head : ListNode) -> ListNode:

        prev = head_new = ListNode(0)
        prev.next = head

        while prev.next and prev.next.next:
            first, second = prev.next, prev.next.next

            prev.next, first.next, second.next, prev = second, second.next, first, first

        return head_new.next


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
        string += str(head.val) + ', '
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