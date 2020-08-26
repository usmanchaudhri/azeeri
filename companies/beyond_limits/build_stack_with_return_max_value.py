"""
build a modified stack which will have an additional function to return the max_value in the stack in constant time.
"""
from heapq import heapify, heappush, heappop

class Stack:
    def __init__(self, values):
        self.values = values[:]
        self.elements = list(map(lambda x: x * -1, numbers))
        heapify(self.elements)

    def insert(self, value):
        curr = value
        self.values.append(curr)
        heappush(self.elements, curr)

    def get(self):
        curr_element = self.values.pop()
        self.elements.remove(curr_element * -1)
        return curr_element

    def max_value(self):
        # element = heappop(self.elements)
        return self.elements[0] * -1

numbers = [1, 10, 3, 5, 2, 100, 56]
# numbers.remove(1)
# print(numbers)
# res = list(map(lambda x: x * -1, numbers))
# print(res)

stack = Stack(numbers)
print('heap elements ', stack.elements)
print('stack values ', stack.values)
print('min value in stack', stack.max_value())
print('get stack value ', stack.get())

print('heap elements ', stack.elements)
print('stack elements ', stack.values)
print('min value in stack', stack.max_value())
