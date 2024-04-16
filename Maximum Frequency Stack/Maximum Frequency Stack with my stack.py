'''Frequency stack'''
class Node:
    '''Node'''
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class FreqStack:
    '''Frequency stack'''
    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        '''Adds an element to the top of the stack'''
        self.head = Node(val, self.head)

    def pop(self) -> int:
        """Removes and returns the most frequent element in the stack"""
        maxi = self.get_max()
        prev = None
        current = self.head
        while current:
            if current.data == maxi:
                if not prev:
                    self.head = self.head.next
                else:
                    prev.next = current.next
                return maxi
            prev = current
            current = current.next
        return maxi

    def __str__(self) -> str:
        s = ''
        cur = self.head
        while cur is not None:
            s = str(cur.data) + ' ' +s
            cur = cur.next
        return 'top -> ' + s[::-1] + ' <- bottom'

    def count(self, x: int) -> int:
        '''Counts how many x in stack'''
        counter = 0
        current = self.head
        while current:
            if current.data == x:
                counter += 1
            current = current.next
        return counter

    def get_max(self) -> int:
        '''Returns max counted data in stack'''
        maxi = None
        current = self.head
        maxi_count = 0
        while current:
            cur_count = self.count(current.data)
            if maxi is None or cur_count > maxi_count:
                maxi = current.data
                maxi_count = self.count(maxi)
            current = current.next
        return maxi

if __name__ == '__main__':
    freqStack = FreqStack()
    freqStack.push(4)
    freqStack.push(0)
    freqStack.push(9)
    freqStack.push(3)
    freqStack.push(2)
    freqStack.pop()
    freqStack.push(6)
    freqStack.pop()
    freqStack.push(1)
    freqStack.pop()
    freqStack.push(1)
    freqStack.pop()
    freqStack.push(4)
    freqStack.pop()
    freqStack.pop()
    freqStack.pop()
    freqStack.pop()