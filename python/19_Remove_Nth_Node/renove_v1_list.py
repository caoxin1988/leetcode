class LinkNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def remove_item(self, head, n):
        
        if head is None or head.next is None:
            return None

        l = []
        while head:
            l.append(head)
            head = head.next

        if n == 1:
            ptr1 = l[(n + 1) * (-1)]
            ptr1.next = None
            l.pop()
        elif n == len(l):
            l.pop(0)
        else:
            ptr1 = l[(n + 1) * (-1)]
            ptr2 = l[(n - 1) * (-1)]
            ptr1.next = ptr2
            l.pop(n * (-1))

        return l[0]

def transfor_list_to_string(head):

    if head is None:
        return '[]'

    string = ''
    while head:
        string += str(head.val) + ', '
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
    n = int(input('please input number : '))

    head = transfor_string_to_list(items)

    ptr = Solution().remove_item(head, n)

    ret = transfor_list_to_string(ptr)

    print(ret)

if __name__ == '__main__':
    main()