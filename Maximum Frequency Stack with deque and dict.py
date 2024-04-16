'''Frequency stack'''
from collections import deque, defaultdict
class FreqStack:
    '''Frequency stack'''
    def __init__(self):
        self.deque = deque()
        self.freq = defaultdict(int)

    def push(self, val: int) -> None:
        '''Adds an element to the top of the stack'''
        self.deque.appendleft(val)
        self.freq[val] += 1

    def pop(self) -> int:
        """Removes and returns the most frequent element in the stack"""
        max_freq = max(self.freq.values())
        for val in self.deque:
            if self.freq[val] == max_freq:
                self.deque.remove(val)
                self.freq[val] -= 1
                return val

if __name__ == '__main__':
    freqStack = FreqStack()
    freqStack.push(5) # The stack is [5]
    freqStack.push(7) # The stack is [5,7]
    freqStack.push(5) # The stack is [5,7,5]
    freqStack.push(7) # The stack is [5,7,5,7]
    freqStack.push(4) # The stack is [5,7,5,7,4]
    freqStack.push(5) # The stack is [5,7,5,7,4,5]
    assert freqStack.pop() == 5  # return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
    assert freqStack.pop() == 7 # return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
    assert freqStack.pop() == 5   # return 5, as 5 is the most frequent. The stack becomes [5,7,4].
    assert freqStack.pop() == 4   # return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].
