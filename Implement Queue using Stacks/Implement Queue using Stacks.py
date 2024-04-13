'''Queue implementation'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class MyQueue:
    '''my queue'''
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, x: int) -> None:
        '''add to queue'''
        if not self.head:
            self.tail = Node(x)
            self.head = self.tail
        else:
            self.tail.next = Node(x)
            self.tail = self.tail.next

    def pop(self) -> int:
        '''Delete from queue'''
        data = self.head.data
        if self.head.next:
            self.head = self.head.next
        else:
            self.head = None
        return data
    def peek(self) -> int:
        '''Returns the element at the front of the queue without removing it.'''
        return self.head.data

    def empty(self) -> bool:
        '''Checks if the queue is empty'''
        return not self.head

if __name__ == '__main__':
    myQueue = MyQueue()
    myQueue.push(1); # queue is: [1]
    myQueue.push(2); # queue is: [1, 2] (leftmost is front of the queue)
    assert myQueue.peek() == 1; # return 1
    assert myQueue.pop() == 1; # return 1, queue is [2]
    assert myQueue.empty() is False; # return false