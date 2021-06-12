# Design a stack that supports push, pop, top, and retrieving 
# the minimum element in constant time.

# We can use simple stack and for min value, return min(stack)
# but this will take O(n) time coz min() check min value in whole list

# Logic: maintain 2 stacks, one is main stack and other is minStack
# push --> in minStack, push value only if its top is > value
# pop --> in minStack, pop only if top of minStack == top of main stack
# top --> nothing to do with minStack
# getMin --> if minStack is not empty then return top element else -1

class MinStack:
    def __init__(self) -> None:
        self.stack = []
        self.minStack = []
    
    def push(self, value):
        self.stack.append(value)

        # if minStack is empty or its top value is > value
        if len(self.minStack) == 0 or self.minStack[-1] > value:
            self.minStack.append(value)

    def pop(self):
        if len(self.stack) > 0:
            temp = self.stack.pop()
            if temp == self.minStack[-1]:
                self.minStack.pop()
    
    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        return -1

    def getMin(self):
        if len(self.minStack) > 0:
            return self.minStack[-1]
        return -1
    
    def print_stack(self):
        print(self.stack)
        print()

stack = MinStack()
stack.push(15)
stack.push(8)
stack.push(12)
stack.push(9)
stack.push(17)
stack.print_stack()
print("top element: ", stack.top())
print("min element", stack.getMin())
print("popped element:", stack.pop())
stack.print_stack()