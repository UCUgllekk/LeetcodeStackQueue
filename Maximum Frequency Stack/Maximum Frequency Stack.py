'''Frequency stack'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return f"Node(data={self.data}, next={self.next})"

    def __repr__(self) -> str:
        return f"Node(data={self.data}, next={self.next})"

class FreqStack:

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        '''Adds an element to the top of the stack'''
        if not self.head:
            self.head = Node(val)
        else:
            old_head = self.head
            self.head = Node(val)
            self.head.next = old_head

    def pop(self) -> int:
        ...

    def __str__(self) -> str:
        s = ''
        cur = self.head
        while cur is not None:
            s = str(cur.data) + ' ' +s
            cur = cur.next
        return 'bottom -> '+ s+'<- top'

if __name__ == '__main__':
    freqStack = FreqStack()
    freqStack.push(5) # The stack is [5]
    freqStack.push(7) # The stack is [5,7]
    freqStack.push(5) # The stack is [5,7,5]
    freqStack.push(7) # The stack is [5,7,5,7]
    freqStack.push(4) # The stack is [5,7,5,7,4]
    freqStack.push(5) # The stack is [5,7,5,7,4,5]
    print(freqStack)
    freqStack.pop()   # return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
    freqStack.pop()   # return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
    freqStack.pop()   # return 5, as 5 is the most frequent. The stack becomes [5,7,4].
    freqStack.pop()   # return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].
