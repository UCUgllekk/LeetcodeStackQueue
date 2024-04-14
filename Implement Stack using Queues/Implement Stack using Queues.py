'''Stack implementation'''
class Node:
    '''Node'''
    def __init__(self, data):
        self.data = data
        self.next = None

class MyStack:
    '''My stack'''
    def __init__(self):
        self.head = None

    def push(self, x: int) -> None:
        '''Adds an element to the top of the stack'''
        old_head = self.head
        self.head = Node(x)
        self.head.next = old_head

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

if __name__ == '__main__':
    myStack = MyStack()
    myStack.push(1)
    myStack.push(2)
    assert myStack.top() == 2; # return 2
    assert myStack.pop() == 2; # return 2
    assert myStack.empty() is False; # return False
