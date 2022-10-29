class MinMaxStack:
    class Node:
        def __init__(self, value, min, max, next):
            self.value = value
            self.min = min
            self.max = max
            self.next = next

    def __init__(self):
        self.head = None

    def peek(self):
        return self.head.value
    
    def push(self, value):
        if self.head == None:
            self.head = MinMaxStack.Node(value, value, value, None)
        else:
            self.head = MinMaxStack.Node(value, min(self.head.min, value), max(self.head.max, value), self.head)

    def pop(self):
        popVal = self.head.value
        self.head = self.head.next
        return popVal
    
    def getMin(self):
        return self.head.min

    def getMax(self):
        return self.head.max

def test_min_max_stack():
    def testMinMaxPeek(min, max, peek, stack):
        assert (stack.getMin() == min)
        assert (stack.getMax() == max)
        assert (stack.peek() == peek)

    stack = MinMaxStack()
    stack.push(5)
    testMinMaxPeek(5, 5, 5, stack)
    stack.push(7)
    testMinMaxPeek(5, 7, 7, stack)
    stack.push(2)
    testMinMaxPeek(2, 7, 2, stack)
    assert (stack.pop() == 2)
    assert (stack.pop() == 7)

