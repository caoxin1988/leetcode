class ListNode(object):
    def __init__(self, x : int):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self):
        self.head = ListNode(0)

    def sort_list(self, head : ListNode):
        if not head:
            return None

        if not head.next:
            return head

        dummy_left = ListNode(0)
        left = dummy_left
        dummy_right = ListNode(0)
        right = dummy_right

        pivot = head.val
        pivot_node = head

        while head:
            if pivot > head.val:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next

            head = head.next

        left.next = None
        right.next = None

        self.head.next = self.sort_list(dummy_left.next)

        ptr = self.head
        while ptr.next:
            ptr = ptr.next

        ptr.next = pivot_node

        pivot_node.next = self.sort_list(dummy_right.next)

        return self.head.next

def transfor_list_to_string(head : ListNode):
    if not head:
        return ''

    string = ''
    while head:
        string += str(head.val) + ', '
        head = head.next

    return '[' + string[:-2] + ']'


def transfor_string_to_list(items: str):
    dummp_ptr = ListNode(0)
    ptr = dummp_ptr

    for item in items:
        ptr.next = ListNode(int(item))
        ptr = ptr.next

    return dummp_ptr.next

def main():
    items = input('please input : ')
    head = transfor_string_to_list(items)

    solution = Solution()
    l = solution.sort_list(head)

    string = transfor_list_to_string(l)

    print(string)


if __name__ == '__main__':
    main()