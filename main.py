class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, value):
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value

stack = Stack()
for x in range(1, 6):
    stack.push(x)

for _ in range(5):
    print(stack.pop())