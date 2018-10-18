
class ArrayStack(object):
    '''
    data : data array for stack
    size : data size this stack can store
    count : current data number in stack
    '''
    def __init__(self, num):
        self.data = list(None for _ in range(1, num))
        self.size = num
        self.count = 0

    def push(self, data):
        '''
        on success, return True; or return False
        '''
        
        if self.count == self.size:
            print('stack is full, push fail')
            return False

        self.count += 1
        self.data[self.count] = data

        print('push element')

        return True

    def pop(self):
        '''
        on success, return value; or return None
        '''
        if self.count == 0:
            return None

        data = self.data[self.count] 
        self.count -= 1

        return data


def main():
    stack = ArrayStack(5)

    stack.push(1)
    stack.push('abc')

    print('data1 : %s' % stack.pop())
    print('data2 : %s' % stack.pop())

    stack.push(4)
    print('data2 : %s' % stack.pop())

if __name__ == '__main__':
    main()