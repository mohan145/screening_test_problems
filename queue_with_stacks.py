class Queue():

    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()


def enqueue(self, element):
    stack_1.push(element)


def dequeque(self):
    if stack_2.isEmpty() and (not stack_1.is_empty()):
        while (not stack_1.isEmpty()):
            element = stack_1.pop()
            stack_2.push(element)

    if stack_2.isEmpty():
        return "Queue Empty"

    return stack_2.pop()