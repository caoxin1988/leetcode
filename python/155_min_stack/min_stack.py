class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min = []
    
    def push(self, x):
        if not self.stack or x <= self.min[-1]:
            self.min.append(x)
            
        self.stack.append(x)

    def pop(self):
        x = self.stack.pop()

        if x == self.min[-1]:
            self.min.pop()

        return x

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min[-1]

minstack = MinStack()
minstack.push(-2)
minstack.push(0)
minstack.push(-3)

print(minstack.get_min())

print(minstack.pop())
print(minstack.pop())


print(minstack.get_min())