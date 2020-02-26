class Stack():

    def __init__(self):
        self.stack = []
        self.top = -1

    def pop(self):
        if self.top == -1:
            return "Stack Empty"
        top_element = self.stack[self.top]
        self.top -= 1
        self.stack.pop()
        return top_element

    def push(self, element):
        self.top += 1
        self.stack.append(element)


