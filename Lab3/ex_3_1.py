class Stack:
    def __init__(self):
        self.stack = []
        self.stack_max = []
        self.stack_min = []
    def push(self, n):
        self.stack.append(n)
        if not self.stack_max or n >= self.stack_max[-1]:
            self.stack_max.append(n)
        else:
            self.stack_max.append(self.stack_max[-1])
        if not self.stack_min or n <= self.stack_min[-1]:
            self.stack_min.append(n)
        else:
            self.stack_min.append(self.stack_min[-1])
    def pop(self):
        self.stack_max.pop()
        self.stack_min.pop()
        return self.stack.pop()
    def max(self):
        return self.stack_max[-1]
    def min(self):
        return self.stack_min[-1]

s = Stack()
s.push(1)
s.push(5)
print(s.max()) # should print 5
s.push(9)
print(s.pop()) # should print 9
s.push(2)
print(s.max()) # should print 5