
class LinkNode(object):
    def __init__(self, data):
        self.data = data
        self.prev = None

class LinkStack(object):
    def __init__(self):
        self.top = None

    def push(self, data):
        node = LinkNode(data)
        node.prev = self.top
        self.top = node

        return True

    def pop(self):
        if self.top is None:
            return None

        node = self.top
        self.top = self.top.prev

        return node

def main():
    stack = LinkStack()

    stack.push(1)
    stack.push('abc')

    node = stack.pop()
    if node:
        print('data : %s' % node.data)
    else:
        print('Stack is None')
    node = stack.pop()
    if node:
        print('data : %s' % node.data)
    else:
        print('Stack is None')
    node = stack.pop()
    if node:
        print('data : %s' % node.data)
    else:
        print('Stack is None')

    stack.push('def')
    node = stack.pop()
    if node:
        print('data : %s' % node.data)
    else:
        print('Stack is None')
    node = stack.pop()
    if node:
        print('data : %s' % node.data)
    else:
        print('Stack is None')

if __name__ == '__main__':
    main()