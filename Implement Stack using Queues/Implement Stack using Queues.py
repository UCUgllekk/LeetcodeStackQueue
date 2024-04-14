'''Stack implementation'''
class Node:
    '''Node'''
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return f"Node(data={self.data}, next={self.next})"
class Queue:
    '''Queue'''
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        '''Returns True if queue is empty'''
        return self.head is None

    def add(self, item):
        '''Add elements to queue'''
        if self.head is None:
            self.tail = Node(item)
            self.head = self.tail
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next

    def pop(self):
        '''Pops last element from queue'''
        if self.head:
            data = self.head.data
            self.head = self.head.next
            return data
        raise ValueError('Queue is empty.')

    @property
    def peek(self):
        '''Returns first element in queue'''
        return self.tail.data

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def __str__(self):
        s = ''
        current = self.head
        while current is not None:
            s += str(current.data)+' '
            current = current.next
        return f'start -> {s}<- end'

class MyStack:
    '''My stack'''
    def __init__(self):
        self.first_queue = Queue()
        self.second_queue = Queue()

    def push(self, x: int) -> None:
        '''Adds an element to the top of the stack'''
        self.first_queue.add(x)

    def pop(self) -> int:
        '''Removes the top element from the stack'''
        if self.first_queue.head is not None:
            for _ in range(len(self.first_queue)-1):
                self.second_queue.add(self.first_queue.pop())
            output = self.first_queue.pop()
            self.second_queue, self.first_queue = self.first_queue, self.second_queue
            return output

    def top(self) -> int:
        '''Returns data of head'''
        return self.first_queue.peek

    def empty(self) -> bool:
        '''Checks if the stack is empty'''
        return self.second_queue.is_empty() and self.first_queue.is_empty()

    def __str__(self) -> str:
        return f"{self.first_queue}, {self.second_queue}"

if __name__ == '__main__':
    myStack = MyStack()
    myStack.push(1)
    myStack.push(2)
    assert myStack.top() == 2; # return 2
    assert myStack.pop() == 2; # return 2
    assert myStack.empty() is False; # return False
