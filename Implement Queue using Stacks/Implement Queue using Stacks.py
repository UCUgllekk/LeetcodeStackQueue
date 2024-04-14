'''Queue implementation'''
class Node:
    '''Node'''
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return f"Node(data={self.data}, next={self.next})"

class Stack:
    '''My stack'''
    def __init__(self):
        self.head = None

    def push(self, x: int) -> None:
        '''Adds an element to the top of the stack'''
        self.head = Node(x, self.head)

    def pop(self) -> int:
        '''Removes the top element from the stack'''
        data = self.head.data
        self.head = self.head.next
        return data

    def top(self) -> int:
        '''Returns data of head'''
        return self.head.data

    def empty(self) -> bool:
        '''Checks if the stack is empty'''
        return not self.head

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count +=1
            current = current.next
        return count

    def __str__(self) -> str:
        return f"{self.head}"

class MyQueue:
    '''my queue'''
    def __init__(self):
        self.head = Stack()
        self.tail = Stack()

    def push(self, x: int) -> None:
        '''add to queue'''
        self.head.push(x)

    def pop(self) -> int:
        '''Delete from queue'''
        if self.tail.empty():
            for _ in range(len(self.head)):
                self.tail.push(self.head.pop())
        return self.tail.pop()

    def peek(self) -> int:
        '''Returns the element at the front of the queue without removing it.'''
        if not self.tail.empty():
            return self.tail.top()
        current = self.head.head
        while current:
            if current.next is None:
                return current.data
            current = current.next

    def empty(self) -> bool:
        '''Checks if the queue is empty'''
        return self.head.empty() and self.tail.empty()

    def __str__(self) -> str:
        return f"head={self.head}, tail={self.tail}"

if __name__ == '__main__':
    myQueue = MyQueue()
    myQueue.push(1); # queue is: [1]
    myQueue.push(2); # queue is: [1, 2] (leftmost is front of the queue)
    assert myQueue.peek() == 1; # return 1
    assert myQueue.pop() == 1; # return 1, queue is [2]
    assert myQueue.empty() is False; # return false