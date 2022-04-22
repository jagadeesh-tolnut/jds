class Stack:

    # Stack using list
    def __init__(self):
        self.data = []

    def length(self):
        # returns the length of the stack
        return len(self.data)

    def is_empty(self):
        # returns boolean (True- empty, False- not empty)
        return len(self.data) == 0

    def push(self,element):
        # inserting element in top of the stack
        self.data.append(element)

    def pop(self):
        # removing the top element
        if self.is_empty():
            raise Exception("Stack is Empty")
        else:
            return self.data.pop()

    def top(self):
        # returning the top element
        if self.is_empty():
            raise Exception("Stack is Empty")
        else:
            return self.data[-1]

