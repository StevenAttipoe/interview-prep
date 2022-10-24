

class MyStack:
    def __init__(self):
        self.queue = []

    def pop(self) -> int:
        return self.queue.pop()

    def push(self, num: int):
        self.queue.append(num)

    def top(self)  -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return self.queue == []

def test():
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    param_2 = obj.pop()
    param_3 = obj.top()
    param_4 = obj.empty()

    assert param_2 == 2
    assert param_3 == 1
    assert param_4 == False