'''Frequency stack'''
from collections import deque
class FreqStack:
    '''Frequency stack'''
    def __init__(self):
        self.deque = deque()
        self.freq = deque()

    def push(self, val: int) -> None:
        '''Adds an element to the top of the stack'''
        self.deque.appendleft(val)

    def pop(self) -> int:
        """Removes and returns the most frequent element in the stack"""
        maxi = self.get_max()
        counter = 0
        for _ in range(len(self.deque)):
            if self.deque[0] == maxi:
                self.deque.popleft()
                self.deque.rotate(counter)
                return maxi
            self.deque.rotate(-1)
            counter += 1

    def __str__(self) -> str:
        return f"{self.deque}"

    def get_max(self) -> int:
        maxi = max(self.deque.count(i) for i in self.deque)
        for i in self.deque:
            if self.deque.count(i) == maxi:
                return i
        # maxi = None
        # for i in self.deque:
        #     if maxi is None or self.deque.count(i) > maxi_count:
        #         maxi = i
        #         maxi_count = self.deque.count(maxi)
        # return maxi

if __name__ == '__main__':
    freqStack = FreqStack()
    freqStack.push(5) # The stack is [5]
    freqStack.push(7) # The stack is [5,7]
    freqStack.push(5) # The stack is [5,7,5]
    freqStack.push(7) # The stack is [5,7,5,7]
    freqStack.push(4) # The stack is [5,7,5,7,4]
    freqStack.push(5) # The stack is [5,7,5,7,4,5]
    print(freqStack)
    assert freqStack.pop() == 5  # return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
    print(freqStack)
    assert freqStack.pop() == 7 # return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
    print(freqStack)
    assert freqStack.pop() == 5   # return 5, as 5 is the most frequent. The stack becomes [5,7,4].
    print(freqStack)
    assert freqStack.pop() == 4   # return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].
    print(freqStack)