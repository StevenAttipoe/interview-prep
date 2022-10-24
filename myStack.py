class MyStack:
    
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        while (len(self.queue1) > 1):
            front = self.queue1.pop(0)
            self.queue2.append(front)
        
        rear = self.queue1.pop(0)
        temp = self.queue1
        self.queue1 = self.queue2
        self.queue2 = temp
        
        return rear
        

    def top(self) -> int:
        return self.queue1[-1]

    def empty(self) -> bool:
        if len(self.queue1) == 0:
            return True
        return False
        
        
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