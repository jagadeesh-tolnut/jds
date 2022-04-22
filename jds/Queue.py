class Queue:
    #  Queue using list
    def __init__(self):
        # attributes of queue
        self.data = []
        self.start = 0
        self.size = 0

    def __len__(self):
        # returns length of queue
        return self.size

    def is_empty(self):
        # returns boolean (True- empty, False- not empty)
        return self.size==0

    def enqueue(self,element):
        # Inserting element in last position
        self.data.append(element)
        self.size += 1

    def dequeue(self):
        # Removing and returning first element
        if self.is_empty():
            Exception("Queue is empty")
        else:
            deq_ele = self.data[self.start]
            self.data[self.start] = None
            self.start += 1
            self.size -= 1
            return deq_ele

    def first(self):
        # Returning the first element
        if self.is_empty():
            Exception("Queue is empty")
        else:
            return self.data[self.start]

    def last(self):
        # returning the last element
        if self.is_empty():
            Exception("Queue is empty")
        else:
            return self.data[(self.start + self.size)-1]