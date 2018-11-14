
class MyStack:
    def __init__(self):
        self.queue = []

    def push(self, x):
        queue_tmp = []

        queue_tmp.append(x)
        while self.queue:
            queue_tmp.append(self.queue.pop(0))

        self.queue = queue_tmp

    def pop(self):
        return self.queue.pop(0)

    def top(self):
        return self.queue[0]

    def empty(self):
        return not self.queue

stack = MyStack()
stack.push(1)
stack.push(2)

print(stack.top())
print(stack.pop())


print(stack.top())
print(stack.empty())


print(stack.pop())
print(stack.empty())