class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        self.in_stack.append(x)

    def pop(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        return self.out_stack.pop()

    def peek(self):
        if self.out_stack:
            return self.out_stack[len(self.out_stack)-1]
        else:
            return self.in_stack[0]

    def empty(self):
        return not self.in_stack and not self.out_stack

queue = MyQueue()
queue.push(1)
queue.push(2)
print(queue.peek())
print(queue.pop())
print(queue.empty())

print(queue.peek())
print(queue.pop())
print(queue.empty())